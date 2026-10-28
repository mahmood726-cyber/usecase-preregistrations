"""Second-reviewer check with agy (Gemini, google family) on a seeded sample, blind to Codex's answers.
FT sample: per pilot, full-text-screened records ordered by sha256('<seed>|<pilot>|agycheck|<key>'); take up to
N_ELIG with final status ELIGIBLE and N_OTHER others (pre-specified here before any agy output is seen).
TA sample: N_TA stage-B records ordered by the same digest. agy gets the same RULES files and source text.
usage: python -I agy_review.py <pilot> [N_ELIG N_OTHER N_TA]"""
import hashlib, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.environ.get("AGY_DRIVER_DIR", os.path.expanduser(os.path.join("~", "agy-driver"))))
import screen, drive, decide
from agy_driver import AgyDriver

SEEDS = {"P14": "2026102714", "P06": "2026102706"}

def digest(p, key): return hashlib.sha256(f"{SEEDS[p]}|{p}|agycheck|{key}".encode()).hexdigest()

def parse_json(text):
    m = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S) or re.findall(r"(\{.*\})", text, re.S)
    for cand in reversed(m):
        try: return json.loads(cand)
        except Exception: continue
    return None


def ask_until_json(drv, prompt, workspace=None, hard_timeout=1500, idle=180):
    """agy's wait_for_response returns at the first quiet gap between tool calls; keep tailing the same
    conversation until a parseable JSON answer appears, or nothing changes for `idle` seconds."""
    import time
    drv.ensure_daemon()
    cid = drv.new_conversation(prompt, model="pro", workspace=workspace, timeout=300)
    t0 = time.time(); last_sig, last_change = None, time.time(); nudges = 0
    while time.time() - t0 < hard_timeout:
        steps = drv._read_steps(cid)
        lu = max((i for i, s in enumerate(steps) if s.get("type") == "USER_INPUT"), default=-1)
        turn = steps[lu + 1:]
        res = drv._assemble(cid, turn, complete=False)
        texts = [(s.get("content") or "") for s in turn if s.get("source") == "MODEL"]
        final = texts[-1] if texts else ""
        busy = any(s.get("status") == "IN_PROGRESS" for s in turn)
        if not busy and parse_json(final) is not None:
            res["complete"] = True; res["final_text"] = final; return res
        sig = (len(turn), sum(len(x) for x in texts))
        if sig != last_sig: last_sig, last_change = sig, time.time()
        elif time.time() - last_change > idle and not busy:
            if nudges < 2:  # agy sometimes stops after reading files; ask for the answer in the same conversation
                nudges += 1
                drv.send_message(cid, "You have read the files. Now reply with ONLY the single JSON object required (no prose, no tools).", workspace=workspace)
                last_sig, last_change = None, time.time(); continue
            res["final_text"] = final; return res
        time.sleep(3)
    res["final_text"] = ""; return res

def main():
    p = sys.argv[1]
    n_elig, n_other, n_ta = (int(x) for x in sys.argv[2:5]) if len(sys.argv) > 4 else (8, 7, 50)
    out_dir = os.path.join(screen.HERE, p, "agy"); os.makedirs(out_dir, exist_ok=True)
    L = screen.read_ledger(p); st = drive.status_table(p)
    ft = sorted([e for (r, s), e in L.items() if s == "C" and "facts" in e], key=lambda e: digest(p, e["key"]))
    elig = [e for e in ft if st[e["rank"]][0] == "ELIGIBLE"][:n_elig]
    other = [e for e in ft if st[e["rank"]][0] != "ELIGIBLE"][:n_other]
    sample = {"ft": [e["rank"] for e in elig + other],
              "ta": [e["rank"] for e in sorted([e for (r, s), e in L.items() if s == "B" and e["decision"] in ("FULLTEXT", "EXCLUDE")],
                                                key=lambda e: digest(p, e["key"]))[:n_ta]]}
    sp = os.path.join(out_dir, "sample.json")
    if os.path.exists(sp):
        sample = json.load(open(sp))  # the sample is fixed at first draw; never redrawn
    else:
        sample["drawn_utc"] = screen.now(); json.dump(sample, open(sp, "w"), indent=1)
    drv = AgyDriver()
    schema_ft = open(os.path.join(screen.HERE, "schema_ft.json")).read()
    res_path = os.path.join(out_dir, "agy_ft.jsonl")
    done = {json.loads(l)["rank"] for l in open(res_path, encoding="utf-8") if json.loads(l).get("facts") and json.loads(l).get("title_ok")} if os.path.exists(res_path) else set()
    for rank in sample["ft"]:
        if rank in done: continue
        src = os.path.join(screen.HERE, p, "ft", f"r{rank:05d}")
        ws = os.path.join(out_dir, f"r{rank:05d}"); os.makedirs(ws, exist_ok=True)
        for fn in ("paper.txt", "record.json"): shutil.copy(os.path.join(src, fn), ws)
        shutil.copy(os.path.join(screen.HERE, "RULES_FT.md"), ws)
        open(os.path.join(ws, "schema_ft.json"), "w").write(schema_ft)
        prompt = (f"Working directory {ws}. Read RULES_FT.md, record.json and ALL of paper.txt there (read it in chunks). "
                  "Apply RULES_FT.md exactly. Reply with ONLY one JSON object with exactly the keys of schema_ft.json "
                  "(enum values as listed there) PLUS one extra key \"paper_title\" holding the TITLE line of THIS paper.txt copied verbatim. "
                  "This is a new paper: ignore any paper from earlier conversations. Do not modify any file.")
        r = ask_until_json(drv, prompt, workspace=ws)
        txt = r.get("final_text") or ""
        facts = parse_json(txt)
        rec_title = json.load(open(os.path.join(ws, "record.json"), encoding="utf-8"))["title"]
        norm = lambda t: re.sub(r"[^a-z0-9]+", "", re.sub(r"<[^>]+>", "", (t or "")).lower())
        title_ok = bool(facts) and norm(facts.get("paper_title")) != "" and (
            norm(facts.get("paper_title")) in norm(rec_title) or norm(rec_title) in norm(facts.get("paper_title")))
        if facts and not title_ok:  # wrong-document guard: an answer about another paper is discarded, not scored
            facts = None
        row = {"rank": rank, "raw": txt[-6000:], "facts": facts, "title_ok": title_ok}
        if facts:
            try: row["agy_status"] = decide.decide(p, facts)[:2]
            except Exception as ex: row["agy_status"] = ["PARSE_INCOMPLETE", str(ex)]
        with open(res_path, "a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print("agy FT", rank, row.get("agy_status"), flush=True)
    # TA: inline abstracts in chunks well under the 32 KB argv limit
    ta_path = os.path.join(out_dir, "agy_ta.jsonl")
    answered = {json.loads(l)["rank"] for l in open(ta_path, encoding="utf-8")} if os.path.exists(ta_path) else set()
    if len(answered) < len(sample["ta"]):
        frame = {r["rank"]: r for r in screen.load_frame(p)}
        rules = open(os.path.join(screen.HERE, "RULES_TA.md"), encoding="utf-8").read()
        chunk, size = [], 0
        def flush(chunk):
            body = "\n".join(chunk)
            prompt = (rules + f"\n\nPILOT: {p}\n\n" + body + "\n\nReply with ONLY a JSON object "
                      '{"records":[{"rank":int,"decision":"FULLTEXT|EXCLUDE","reason_code":"NONE|NOT_MA|DESIGN|POPULATION|K_LT_10","reason":str}]}. Do not use tools.')
            r = ask_until_json(drv, prompt)
            j = parse_json(r.get("final_text") or "") or {"records": []}
            with open(ta_path, "a", encoding="utf-8") as f:
                for e in j.get("records", []): f.write(json.dumps(e, ensure_ascii=False) + "\n")
            print("agy TA chunk", len(j.get("records", [])), flush=True)
        for rank in [x for x in sample["ta"] if x not in answered]:
            r = frame[rank]
            ab = re.sub(r"<[^>]+>", " ", r.get("abstractText") or "(no abstract)")[:3500]
            item = f"=== rank {rank} ===\nTITLE: {r['title']}\nYEAR: {r['pubYear']}  PUBTYPES: {r.get('pubTypes')}\nABSTRACT: {ab}\n"
            if size + len(item) > 20000:
                flush(chunk); chunk, size = [], 0
            chunk.append(item); size += len(item)
        if chunk: flush(chunk)

if __name__ == "__main__":
    main()
