"""Deduplicate each frame exactly as the drafts specify (DOI -> PMID -> normalized title+first author+year),
then order by the seeded SHA-256 rule. Writes <pilot>_frame_ordered.jsonl and <pilot>_dedup_log.json."""
import glob, hashlib, json, os, re, sys, unicodedata

OUT = sys.argv[1]
SEEDS = {"P14": "2026102714", "P06": "2026102706"}

def norm_doi(d):
    if not d: return None
    d = d.strip().lower()
    d = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:\s*", "", d)
    return d or None

def norm_title(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", t)).strip()

def first_author(r):
    al = (r.get("authorList") or {}).get("author") or []
    if al:
        a = al[0]
        s = a.get("lastName") or a.get("collectiveName") or a.get("fullName") or ""
    else:
        s = (r.get("authorString") or "").split(",")[0].split(" ")[0]
    return norm_title(s)

for pilot, seed in SEEDS.items():
    recs = [x for f in sorted(glob.glob(os.path.join(OUT, pilot, "*.json")))
            for x in json.load(open(f, encoding="utf-8"))["resultList"]["result"]]
    n = len(recs)
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[max(ra, rb)] = min(ra, rb)
    keys = []
    for i, r in enumerate(recs):
        keys.append({"doi": norm_doi(r.get("doi")), "pmid": (r.get("pmid") or None),
                     "tkey": f"{norm_title(r.get('title'))}|{first_author(r)}|{r.get('pubYear')}"})
    reasons = []
    for field in ("doi", "pmid", "tkey"):
        seen = {}
        for i, k in enumerate(keys):
            v = k[field]
            if not v: continue
            if v in seen:
                if find(i) != find(seen[v]):
                    reasons.append({"field": field, "value": v, "ids": [recs[seen[v]].get("id"), recs[i].get("id")]})
                union(i, seen[v])
            else:
                seen[v] = i
    groups = {}
    for i in range(n): groups.setdefault(find(i), []).append(i)
    rows = []
    for g in groups.values():
        # representative: prefer record with pmcid, then MED source, then lowest id
        g.sort(key=lambda i: (recs[i].get("pmcid") is None, recs[i].get("source") != "MED", str(recs[i].get("id"))))
        dois = sorted({keys[i]["doi"] for i in g if keys[i]["doi"]})
        pmids = sorted({keys[i]["pmid"] for i in g if keys[i]["pmid"]})
        if dois: ck = "doi:" + dois[0]
        elif pmids: ck = "pmid:" + pmids[0]
        else: ck = "title:" + keys[g[0]]["tkey"]
        r = recs[g[0]]
        digest = hashlib.sha256(f"{seed}|{pilot}|{ck}".encode("utf-8")).hexdigest()
        rows.append({"canonical_key": ck, "sha256_rank_digest": digest, "member_ids": [recs[i].get("id") for i in g],
                     "id": r.get("id"), "source": r.get("source"), "pmid": r.get("pmid"), "pmcid": r.get("pmcid"),
                     "doi": r.get("doi"), "title": r.get("title"), "authorString": r.get("authorString"),
                     "journal": ((r.get("journalInfo") or {}).get("journal") or {}).get("title"),
                     "pubYear": r.get("pubYear"), "firstPublicationDate": r.get("firstPublicationDate"),
                     "license": r.get("license"), "inEPMC": r.get("inEPMC"), "isOpenAccess": r.get("isOpenAccess"),
                     "pubTypes": ((r.get("pubTypeList") or {}).get("pubType") or []),
                     "abstractText": r.get("abstractText")})
    rows.sort(key=lambda x: (x["sha256_rank_digest"], x["canonical_key"]))
    for k, x in enumerate(rows, 1): x["rank"] = k
    with open(os.path.join(OUT, f"{pilot}_frame_ordered.jsonl"), "w", encoding="utf-8") as f:
        for x in rows: f.write(json.dumps(x, ensure_ascii=False) + "\n")
    log = {"pilot": pilot, "seed": seed, "records_raw": n, "records_deduplicated": len(rows),
           "duplicates_removed": n - len(rows), "merge_events": reasons,
           "rule": "union-find on normalized DOI, then PMID, then normalized title|first author|pubYear; canonical key doi:>pmid:>title:; rank = ascending sha256('seed|pilot|key'), ties by key"}
    json.dump(log, open(os.path.join(OUT, f"{pilot}_dedup_log.json"), "w", encoding="utf-8"), indent=1)
    print(pilot, n, "->", len(rows), "merges", len(reasons))
