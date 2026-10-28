"""Seeded-order eligibility screening orchestrator (pc2 coordinates; Codex workers do the judgement).

Stages, in this order for every record (the first failing stage gives the logged reason):
  A  mechanical metadata gate: Europe PMC full text (PMCID) present; licence documented as CC BY / CC BY-SA / CC0
     (index field, or the full-text <license> when the index field is empty); not a correction/retraction notice.
  B  Codex title/abstract screen (RULES_TA.md), batches of 25.
  F  fetch Europe PMC fullTextXML (fail closed), confirm licence at source, convert to paper.txt.
  C  Codex full-text screen (RULES_FT.md), one record per exec.
Ledger: <pilot>/ledger.jsonl, one line per (rank, stage). Resumable. No trial data are extracted.

usage: python -I screen.py <pilot> <max_rank> [workers]
"""
import concurrent.futures as cf, hashlib, json, os, re, subprocess, sys, time, datetime, urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path: sys.path.insert(0, HERE)  # -I drops the script dir; decide.py lives here
FRAMES = os.path.dirname(HERE)
OK_LIC = {"cc by", "cc by-sa", "cc0"}
import shutil as _sh
CODEX = [_sh.which("codex") or "codex", "exec", "--skip-git-repo-check", "-s", "read-only"]
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

def load_frame(p):
    return [json.loads(l) for l in open(os.path.join(FRAMES, f"{p}_frame_ordered.jsonl"), encoding="utf-8")]

def ledger_path(p): return os.path.join(HERE, p, "ledger.jsonl")

def read_ledger(p):
    out = {}
    if os.path.exists(ledger_path(p)):
        for l in open(ledger_path(p), encoding="utf-8"):
            e = json.loads(l); out[(e["rank"], e["stage"])] = e
    return out

def append(p, e):
    e["utc"] = now()
    with open(ledger_path(p), "a", encoding="utf-8") as f: f.write(json.dumps(e, ensure_ascii=False) + "\n")

def norm_lic(s):
    s = (s or "").lower()
    s = s.replace("creative commons attribution", "cc by")
    return s

# ---------- stage A ----------
NOTICE = re.compile(r"^(correction|erratum|corrigendum|retraction|retracted|expression of concern|notice of retraction)\b", re.I)
def stage_a(r):
    pts = [t.lower() for t in r.get("pubTypes") or []]
    if any("erratum" in t or "retraction" in t or "expression of concern" in t for t in pts) or NOTICE.match(r.get("title") or ""):
        return "EXCLUDE", "A_NOTICE", f"pubTypes={pts}"
    if not r.get("pmcid"):
        return "EXCLUDE", "A_NO_EPMC_FULLTEXT", "no PMCID in Europe PMC record"
    # AM-S1b (2026-10-27): licence is recorded, not a gate; free readability = Europe PMC open-access full text
    lic = (r.get("license") or "").lower()
    return "PASS", "NONE", f"index licence '{lic or 'none recorded in index'}' (recorded only)"

# ---------- codex helper ----------
def run_codex(workdir, prompt, schema, timeout=900, extra=()):
    out = os.path.join(workdir, "codex_out.json")
    if os.path.exists(out): os.remove(out)
    cmd = CODEX + list(extra) + ["-C", workdir, "--output-schema", schema, "-o", out, prompt]
    with open(os.path.join(workdir, "codex_stdout.log"), "wb") as lf:
        try:
            rc = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=lf, stderr=subprocess.STDOUT, timeout=timeout).returncode
        except subprocess.TimeoutExpired:
            return None, "TIMEOUT"
    log = open(os.path.join(workdir, "codex_stdout.log"), encoding="utf-8", errors="replace").read()
    if "out of credits" in log or "insufficient_quota" in log:
        raise SystemExit("CODEX CREDITS EXHAUSTED: " + workdir)
    if not os.path.exists(out):
        return None, f"NO_OUTPUT rc={rc}"
    try:
        return json.load(open(out, encoding="utf-8")), None
    except Exception as e:
        return None, f"BAD_JSON {e}"

# ---------- stage B ----------
def stage_b_batch(p, batch):
    bdir = os.path.join(HERE, p, "ta", f"batch_{batch[0]['rank']:05d}_{batch[-1]['rank']:05d}")
    os.makedirs(bdir, exist_ok=True)
    with open(os.path.join(bdir, "records.txt"), "w", encoding="utf-8") as f:
        f.write(f"PILOT: {p}\n\n")
        for r in batch:
            ab = re.sub(r"<[^>]+>", " ", r.get("abstractText") or "(no abstract)")
            f.write(f"=== rank {r['rank']} ===\nTITLE: {r['title']}\nYEAR: {r['pubYear']}  JOURNAL: {r['journal']}\nPUBTYPES: {r.get('pubTypes')}\nABSTRACT: {ab}\n\n")
    import shutil; shutil.copy(os.path.join(HERE, "RULES_TA.md"), bdir)
    prompt = ("Read RULES_TA.md and records.txt in the current directory. Screen every record in records.txt "
              f"for pilot {p} following RULES_TA.md exactly. Return JSON matching the output schema with one entry per record.")
    res, err = run_codex(bdir, prompt, os.path.join(HERE, "schema_ta.json"))
    if err: return {r["rank"]: {"decision": "ERROR", "reason_code": "B_" + err.split()[0], "reason": err} for r in batch}
    got = {e["rank"]: e for e in res["records"]}
    return {r["rank"]: got.get(r["rank"], {"decision": "ERROR", "reason_code": "B_MISSING", "reason": "rank absent from output"}) for r in batch}

# ---------- fetch + convert ----------
def txt(e): return re.sub(r"\s+", " ", "".join(e.itertext())).strip() if e is not None else ""

def jats_to_text(xml):
    root = ET.fromstring(xml)
    out = []
    t = root.find(".//article-meta/title-group/article-title"); out.append("TITLE: " + txt(t))
    for lic in root.iter("license"):
        out.append(f"LICENSE ELEMENT: href={lic.get('{http://www.w3.org/1999/xlink}href')} type={lic.get('license-type')} :: {txt(lic)[:400]}")
    for d in root.findall(".//article-meta/pub-date"):
        out.append("PUB-DATE " + str(d.attrib) + ": " + txt(d))
    ab = root.find(".//article-meta/abstract"); out.append("\nABSTRACT: " + txt(ab))
    def walk(node, depth):
        for ch in node:
            tag = ch.tag
            if tag == "sec":
                out.append("\n" + "#" * min(depth + 1, 5) + " " + txt(ch.find("title"))); walk(ch, depth + 1)
            elif tag == "p":
                # inline figs/tables inside paragraphs
                out.append(txt(ch))
                for sub in ch:
                    if sub.tag in ("fig", "table-wrap", "supplementary-material"): emit(sub)
            elif tag in ("fig", "table-wrap", "supplementary-material", "fig-group", "table-wrap-group"):
                emit(ch)
            elif tag in ("list", "boxed-text", "disp-quote"):
                out.append(txt(ch))
    def emit(e):
        if e.tag in ("fig-group", "table-wrap-group"):
            for c in e: emit(c)
            return
        if e.tag == "fig":
            g = e.find(".//graphic")
            href = g.get("{http://www.w3.org/1999/xlink}href") if g is not None else None
            out.append(f"\n[FIGURE id={e.get('id')} label={txt(e.find('label'))} graphic={href}] CAPTION: {txt(e.find('caption'))}")
        elif e.tag == "table-wrap":
            out.append(f"\n[TABLE id={e.get('id')} label={txt(e.find('label'))}] CAPTION: {txt(e.find('caption'))}")
            for tr in e.iter("tr"):
                out.append(" | ".join(txt(c) for c in tr if c.tag in ("td", "th")))
            for fn in e.iter("table-wrap-foot"): out.append("FOOT: " + txt(fn))
            g = e.find(".//graphic")
            if g is not None and not list(e.iter("tr")):
                out.append(f"(table is an IMAGE: graphic={g.get('{http://www.w3.org/1999/xlink}href')})")
        else:
            m = e.find(".//media")
            href = (m.get("{http://www.w3.org/1999/xlink}href") if m is not None else e.get("{http://www.w3.org/1999/xlink}href"))
            out.append(f"\n[SUPPLEMENT id={e.get('id')} href={href}] {txt(e)[:500]}")
    body = root.find(".//body")
    if body is not None:
        out.append("\n=== BODY ==="); walk(body, 0)
    back = root.find(".//back")
    if back is not None:
        for sec in back.findall("./sec"): out.append("\n# BACK: " + txt(sec.find("title"))); walk(sec, 1)
        for e in back.iter():
            if e.tag in ("supplementary-material",): emit(e)
        refs = back.findall(".//ref")
        if refs:
            out.append("\n=== REFERENCES ===")
            for rf in refs: out.append(f"[{rf.get('id')}] {txt(rf)[:300]}")
    for e in root.findall(".//floats-group/*"): emit(e)
    return "\n".join(out)

def fetch_ft(p, r):
    rdir = os.path.join(HERE, p, "ft", f"r{r['rank']:05d}")
    os.makedirs(rdir, exist_ok=True)
    xp = os.path.join(rdir, "fulltext.xml")
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{r['pmcid']}/fullTextXML"
    if not os.path.exists(xp):
        body = None
        for att in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "mma-screen/1.0"}), timeout=120) as resp:
                    body = resp.read()
                if not body.lstrip().startswith(b"<?xml") and b"<article" not in body[:3000]:
                    raise ValueError("not JATS")
                break
            except urllib.error.HTTPError as e:
                if e.code == 404: return None, url, "HTTP404"
                last_code = e.code
                time.sleep(4 * (att + 1)); body = None
            except Exception:
                time.sleep(4 * (att + 1)); body = None
        if body is None:
            lc = locals().get("last_code")
            return None, url, (f"SOURCE_HTTP{lc}" if lc and lc >= 500 else "FETCH_FAILED")
        open(xp, "wb").write(body)
        json.dump({"url": url, "sha256": hashlib.sha256(body).hexdigest(), "pulled_utc": now()}, open(os.path.join(rdir, "fetch.json"), "w"))
    body = open(xp, "rb").read()
    try:
        text = jats_to_text(body)
    except Exception as e:
        return None, url, f"PARSE_FAILED {e}"
    open(os.path.join(rdir, "paper.txt"), "w", encoding="utf-8").write(text)
    meta = {k: r.get(k) for k in ("rank", "canonical_key", "pmcid", "pmid", "doi", "title", "journal", "pubYear", "firstPublicationDate", "license")}
    meta["pilot"] = p
    json.dump(meta, open(os.path.join(rdir, "record.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    lics = re.findall(r"LICENSE ELEMENT: href=(\S*) type=(\S*) :: (.*)", text)
    return {"rdir": rdir, "licenses": lics, "chars": len(text)}, url, None

def source_licence_ok(lics, index_lic):
    """Return (ok, label). Source licence from JATS <license>; must agree with the index or fill its gap."""
    joined = " ".join(" ".join(x) for x in lics).lower()
    if not joined.strip():
        return (index_lic in OK_LIC), f"no <license> in XML; index '{index_lic}'"
    nc = bool(re.search(r"by-nc|noncommercial|non-commercial|by-nd|noderivative|no derivative", joined))
    by = bool(re.search(r"creativecommons\.org/licenses/by/|creativecommons\.org/licenses/by-sa/|publicdomain/zero|cc by 4|cc-by|cc by\b|attribution 4\.0|attribution license|creative commons attribution", joined))
    if nc: return False, "source licence restricts reuse (NC/ND): " + joined[:160]
    if by: return True, "source licence CC BY/BY-SA/CC0: " + joined[:160]
    return False, "source licence not documented as CC BY/BY-SA/CC0: " + joined[:160]

# ---------- stage C ----------
def stage_c(p, info):
    import shutil; shutil.copy(os.path.join(HERE, "RULES_FT.md"), info["rdir"])
    prompt = ("Read RULES_FT.md, record.json and paper.txt in the current directory (paper.txt may be long: read it all, "
              "in chunks if needed). Apply RULES_FT.md exactly and return JSON matching the output schema.")
    return run_codex(info["rdir"], prompt, os.path.join(HERE, "schema_ft.json"), timeout=1200)


# ---------- stage C2 (P14 chronology when C left years unmapped) ----------
def c2_span(c2, k):
    """Deterministic span decision from the years Codex listed (its own arithmetic is not trusted)."""
    ys = sorted(int(y) for y in (c2.get("years") or []))
    if c2.get("method") == "individual" and len(ys) >= 2:
        return ys[0], ys[-1]
    if c2.get("method") == "bound" and k and len(ys) >= k:
        # established iff every k-window of the sorted years spans >= 5; return the tightest window as proof
        w = min(range(len(ys) - k + 1), key=lambda i: ys[i + k - 1] - ys[i])
        return ys[w], ys[w + k - 1]
    return None, None

def facts_for(L, rank):
    """C facts with any C2 chronology correction applied (single source for decide callers)."""
    c = L.get((rank, "C"))
    if not c or "facts" not in c: return None
    f = dict(c["facts"])
    e = L.get((rank, "E"))  # AM-S8 second pass on independence; recomputed from the stored transcription
    if e and e.get("e"):
        import indep
        ind, _ = indep.independence(e["e"], f.get("k_designated"))
        if ind in ("yes", "no"):
            f["independence_ok"] = ind
    c2 = L.get((rank, "C2"))
    if c2 and c2.get("c2"):
        lo, hi = c2_span(c2["c2"], f.get("k_designated"))
        f["trial_years_min"], f["trial_years_max"] = lo, hi
    return f

def stage_c2(p, rank, facts):
    rdir = os.path.join(HERE, p, "ft", f"r{rank:05d}")
    d2 = os.path.join(rdir, "stage_c2"); os.makedirs(d2, exist_ok=True)
    import shutil
    shutil.copy(os.path.join(rdir, "paper.txt"), d2); shutil.copy(os.path.join(HERE, "RULES_C2.md"), d2)
    json.dump({k: facts[k] for k in ("designated_outcome", "designated_comparison", "designated_timepoint", "k_designated", "per_study_location")},
              open(os.path.join(d2, "target.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return run_codex(d2, "Read RULES_C2.md, target.json and paper.txt in the current directory and answer per RULES_C2.md as JSON matching the output schema.",
                     os.path.join(HERE, "schema_c2.json"), timeout=900)

def needs_c2(p, L, rank):
    c = L.get((rank, "C"))
    if p != "P14" or not c or "facts" not in c or (rank, "C2") in L: return False
    f = c["facts"]
    if not (f["trial_years_min"] is None or f["trial_years_max"] is None): return False
    import decide  # only when chronology is the first failing criterion; otherwise C2 cannot change the outcome
    return decide.decide(p, f)[1] == "CHRONOLOGY"

# ---------- main ----------
def main():
    p, max_rank = sys.argv[1], int(sys.argv[2])
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    os.makedirs(os.path.join(HERE, p), exist_ok=True)
    frame = [r for r in load_frame(p) if r["rank"] <= max_rank]
    L = read_ledger(p)
    # A
    for r in frame:
        if (r["rank"], "A") not in L or L[(r["rank"], "A")]["reason_code"] == "A_LICENCE":
            d, c, why = stage_a(r)
            e = {"rank": r["rank"], "key": r["canonical_key"], "stage": "A", "decision": d, "reason_code": c, "reason": why}
            append(p, e); L[(r["rank"], "A")] = e
    # B
    todo = [r for r in frame if L[(r["rank"], "A")]["decision"] == "PASS" and
            ((r["rank"], "B") not in L or L[(r["rank"], "B")]["decision"] == "ERROR")]
    batches = [todo[i:i + 25] for i in range(0, len(todo), 25)]
    with cf.ThreadPoolExecutor(workers) as ex:
        for res in ex.map(lambda b: stage_b_batch(p, b), batches):
            for rank, e in res.items():
                r = next(x for x in frame if x["rank"] == rank)
                ee = {"rank": rank, "key": r["canonical_key"], "stage": "B", "decision": e["decision"],
                      "reason_code": e.get("reason_code"), "reason": e.get("reason")}
                append(p, ee); L[(rank, "B")] = ee
            print("B batch done", flush=True)
    # F + C
    todo = [r for r in frame if L.get((r["rank"], "B"), {}).get("decision") == "FULLTEXT" and
            ((r["rank"], "C") not in L or L[(r["rank"], "C")]["decision"] in ("ERROR",)
             or L[(r["rank"], "C")]["reason_code"] == "F_LICENCE_AT_SOURCE")]
    def do_fc(r):
        info, url, err = fetch_ft(p, r)
        if err:
            dec = "EXCLUDE" if err == "HTTP404" else "UNRESOLVED" if err.startswith("SOURCE_HTTP5") else "ERROR"
            return {"rank": r["rank"], "key": r["canonical_key"], "stage": "C", "decision": dec,
                    "reason_code": "F_NO_FULLTEXT" if err == "HTTP404" else "F_" + err.split()[0], "reason": f"{err} {url}"}
        ok, lab = source_licence_ok(info["licenses"], (r.get("license") or "").lower())  # recorded only (AM-S1b)
        res, err = stage_c(p, info)
        if err:
            return {"rank": r["rank"], "key": r["canonical_key"], "stage": "C", "decision": "ERROR", "reason_code": "C_" + err.split()[0], "reason": err}
        return {"rank": r["rank"], "key": r["canonical_key"], "stage": "C", "decision": res["verdict"],
                "reason_code": res["reason_code"], "reason": res["reason"], "licence_at_source": lab,
                "fulltext_url": url, "facts": res}
    with cf.ThreadPoolExecutor(workers) as ex:
        for e in ex.map(do_fc, todo):
            append(p, e); L[(e["rank"], "C")] = e
            print("C", e["rank"], e["decision"], e["reason_code"], flush=True)
    todo2 = [r for r in frame if needs_c2(p, L, r["rank"])]
    def do_c2(r):
        res, err = stage_c2(p, r["rank"], L[(r["rank"], "C")]["facts"])
        return {"rank": r["rank"], "key": r["canonical_key"], "stage": "C2", "decision": "ERROR" if err else "DONE",
                "reason_code": err or "NONE", "reason": (res or {}).get("basis", ""), "c2": res}
    with cf.ThreadPoolExecutor(workers) as ex:
        for e in ex.map(do_c2, todo2):
            if e["decision"] == "ERROR": print("C2 ERROR", e["rank"], e["reason_code"], flush=True); continue
            append(p, e); L[(e["rank"], "C2")] = e
            print("C2", e["rank"], e["c2"].get("method"), c2_span(e["c2"], L[(e["rank"], "C")]["facts"].get("k_designated")), flush=True)

if __name__ == "__main__":
    main()
