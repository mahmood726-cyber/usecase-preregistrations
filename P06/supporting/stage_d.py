"""Stage D: for records whose text facts leave only per-study display (FIGURE/SUPPLEMENT) or a model label
to confirm, fetch the review's files via the Europe PMC supplementaryFiles API (official OA route) and have
Codex view the designated forest plot / supplement. usage: python -I stage_d.py <pilot> [workers]"""
import concurrent.futures as cf, hashlib, io, json, os, re, sys, time, urllib.request, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import screen, decide

HERE = screen.HERE

def fetch_zip(rdir, pmcid):
    zp = os.path.join(rdir, "files.zip")
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/supplementaryFiles?includeInlineImage=yes"
    if not os.path.exists(zp):
        for att in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "mma-screen/1.0"}), timeout=300) as r:
                    b = r.read()
                zipfile.ZipFile(io.BytesIO(b))  # fail closed on non-zip payloads
                open(zp, "wb").write(b)
                json.dump({"url": url, "sha256": hashlib.sha256(b).hexdigest(), "utc": screen.now()}, open(os.path.join(rdir, "files_fetch.json"), "w"))
                break
            except Exception as e:
                err = str(e); time.sleep(5 * (att + 1))
        else:
            return None, url
    return zipfile.ZipFile(zp), url

def pick_images(rdir, z, loc):
    paper = open(os.path.join(rdir, "paper.txt"), encoding="utf-8").read()
    figs = re.findall(r"\[FIGURE id=(\S*) label=(.*?) graphic=(\S*?)\]", paper)
    names = {n.lower(): n for n in z.namelist()}
    def file_for(g):
        g = g.lower()
        for cand in (g, g + ".jpg", re.sub(r"\.(tif|gif|png)$", ".jpg", g)):
            if cand in names: return names[cand]
        stem = re.sub(r"\.\w+$", "", g)
        for n in names:
            if n.startswith(stem) and n.endswith((".jpg", ".png")): return names[n]
        return None
    loc_l = (loc or "").lower()
    chosen = []
    for fid, lab, g in figs:
        num = re.search(r"(\d+)", lab or "")
        hit = (fid and fid.lower() in loc_l) or (lab and lab.lower() in loc_l) or \
              (num and re.search(r"fig(ure)?\.?\s*" + num.group(1) + r"\b", loc_l))
        if hit:
            fn = file_for(g)
            if fn: chosen.append(fn)
    if not chosen:
        chosen = [f for f in (file_for(g) for _, _, g in figs) if f][:8]
    return chosen

def run_one(p, e):
    f = e["facts"]; rank = e["rank"]
    rdir = os.path.join(HERE, p, "ft", f"r{rank:05d}")
    rec = json.load(open(os.path.join(rdir, "record.json"), encoding="utf-8"))
    z, url = fetch_zip(rdir, rec["pmcid"])
    if z is None:
        return {"source_found": "no", "per_study_printed": "unclear", "trial_rows": None, "plot_model_label": "",
                "plot_weighting": "unstated", "plot_fixed_random": "unstated", "note": "files API fetch failed " + url}
    ddir = os.path.join(rdir, "stage_d"); os.makedirs(ddir, exist_ok=True)
    imgs = pick_images(rdir, z, f["per_study_location"])
    paths = []
    for n in imgs:
        out = os.path.join(ddir, os.path.basename(n)); open(out, "wb").write(z.read(n)); paths.append(out)
    if f["per_study_data"] == "SUPPLEMENT_ONLY":
        sd = os.path.join(ddir, "supp"); os.makedirs(sd, exist_ok=True)
        for n in z.namelist():
            if not n.lower().endswith((".jpg", ".gif", ".png", ".tif")):
                open(os.path.join(sd, os.path.basename(n)), "wb").write(z.read(n))
    json.dump({k: f[k] for k in ("designated_outcome", "designated_comparison", "designated_timepoint", "per_study_data", "per_study_location", "k_designated")},
              open(os.path.join(ddir, "target.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    import shutil; shutil.copy(os.path.join(HERE, "RULES_D.md"), ddir)
    prompt = ("Read RULES_D.md and target.json in the current directory; inspect the attached images" +
              (" and the files in supp/ (use any local tool to read PDF/DOCX/XLSX)" if f["per_study_data"] == "SUPPLEMENT_ONLY" else "") +
              ". Answer per RULES_D.md as JSON matching the output schema.")
    cmd_extra = []
    for pth in paths[:8]: cmd_extra += ["-i", pth]
    res, err = screen.run_codex(ddir, prompt, os.path.join(HERE, "schema_d.json"), timeout=1200, extra=cmd_extra)
    if err:
        return {"source_found": "no", "per_study_printed": "unclear", "trial_rows": None, "plot_model_label": "",
                "plot_weighting": "unstated", "plot_fixed_random": "unstated", "note": "codex " + err, "_error": True}
    res["images_used"] = [os.path.basename(x) for x in paths[:8]]
    return res

def main():
    p = sys.argv[1]; workers = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    L = screen.read_ledger(p)
    todo = []
    for (rank, st), e in sorted(L.items()):
        if st != "C" or "facts" not in e: continue
        if (rank, "D") in L and not L[(rank, "D")].get("d", {}).get("_error"): continue
        f = screen.facts_for(L, rank)
        s, c, n = decide.decide(p, f)
        if s == "PENDING_D": todo.append(dict(e, facts=f))
    print("stage D todo", len(todo), flush=True)
    # ex.map runs the submitted lambdas concurrently but yields results in input order
    with cf.ThreadPoolExecutor(workers) as ex:
        for e, d in zip(todo, ex.map(lambda e: run_one(p, e), todo)):
            s, c, n = decide.decide(p, e["facts"], d)
            screen.append(p, {"rank": e["rank"], "key": e["key"], "stage": "D", "decision": s, "reason_code": c, "reason": n, "d": d})
            print("D", e["rank"], s, c, flush=True)

if __name__ == "__main__":
    main()
