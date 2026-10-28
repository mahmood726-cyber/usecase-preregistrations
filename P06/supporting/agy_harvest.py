"""Harvest late agy answers from conversation transcripts. A conversation is attributed to a record ONLY by the
working directory named in its own first USER_INPUT prompt (never by paths in tool output or injected
history). The last JSON answer in that conversation is title-checked against record.json (wrong-document guard).
Appends verified rows to <pilot>/agy/agy_ft.jsonl. usage: python -I agy_harvest.py <pilot>"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import screen, decide
from agy_review import parse_json

BRAIN = os.path.expanduser(r"~\.gemini\antigravity\brain")
p = sys.argv[1]
adir = os.path.join(screen.HERE, p, "agy")
res_path = os.path.join(adir, "agy_ft.jsonl")
have = {json.loads(l)["rank"] for l in open(res_path, encoding="utf-8") if json.loads(l).get("title_ok")} if os.path.exists(res_path) else set()
sample = json.load(open(os.path.join(adir, "sample.json")))["ft"]
norm = lambda t: re.sub(r"[^a-z0-9]+", "", re.sub(r"<[^>]+>", "", (t or "")).lower())
best = {}
for tp in glob.glob(os.path.join(BRAIN, "*", ".system_generated", "logs", "transcript.jsonl")):
    steps = []
    for l in open(tp, encoding="utf-8", errors="replace"):
        try: steps.append(json.loads(l))
        except Exception: pass
    first = next((s for s in steps if s.get("type") == "USER_INPUT"), None)
    if not first: continue
    m = re.search(r"Working directory (\S+?)[\\/]agy[\\/]r(\d{5})\.", first.get("content") or "")
    if not m or os.path.normcase(os.path.abspath(m.group(1))) != os.path.normcase(os.path.join(screen.HERE, p)): continue
    rank = int(m.group(2))
    if rank not in sample or rank in have: continue
    answers = [s.get("content") for s in steps if s.get("type") == "PLANNER_RESPONSE" and parse_json(s.get("content") or "")]
    if not answers: continue
    facts = parse_json(answers[-1])
    rec_title = json.load(open(os.path.join(adir, f"r{rank:05d}", "record.json"), encoding="utf-8"))["title"]
    ok = norm(facts.get("paper_title")) != "" and (norm(facts.get("paper_title")) in norm(rec_title) or norm(rec_title) in norm(facts.get("paper_title")))
    mt = os.path.getmtime(tp)
    if ok and (rank not in best or mt > best[rank][0]):
        best[rank] = (mt, facts, os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(tp)))))
with open(res_path, "a", encoding="utf-8") as f:
    for rank, (mt, facts, cid) in sorted(best.items()):
        row = {"rank": rank, "raw": "(harvested from transcript)", "facts": facts, "title_ok": True, "conversation_id": cid,
               "agy_status": list(decide.decide(p, facts)[:2])}
        f.write(json.dumps(row, ensure_ascii=False) + "\n"); print("harvested", rank, row["agy_status"])
print("missing:", [r for r in sample if r not in have and r not in best])
