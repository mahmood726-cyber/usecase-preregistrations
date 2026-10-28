"""Pull complete Europe PMC record sets (resultType=core, cursorMark) for the P14/P06 draft queries.
Saves every raw page JSON, a manifest with sha256 + UTC pull time + request URL per page."""
import hashlib, json, sys, time, urllib.parse, urllib.request, datetime, os

OUT = sys.argv[1]
BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
Q = {
 "P14": '(PUB_TYPE:"Meta-Analysis" OR TITLE:"meta-analysis" OR TITLE:"meta analysis") AND (TITLE_ABS:randomized OR TITLE_ABS:randomised OR TITLE_ABS:RCT OR TITLE_ABS:RCTs) AND OPEN_ACCESS:Y AND LANG:eng AND (FIRST_PDATE:[2016-10-27 TO 2016-12-31] OR FIRST_PDATE:[2026-01-01 TO 2026-10-27]) AND (TITLE_ABS:child* OR TITLE_ABS:pediatric* OR TITLE_ABS:paediatric* OR TITLE_ABS:infant* OR TITLE_ABS:neonat* OR TITLE_ABS:adolescen*) sort_date:y',
}
PAGE = 1000

def get(url):
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "mma-frame-pull/1.0"}), timeout=180) as r:
                body = r.read()
            d = json.loads(body)  # fail closed on HTML error payloads
            if "resultList" not in d:
                raise ValueError("no resultList")
            return body, d
        except Exception as e:
            print("retry", attempt, e, file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    raise SystemExit("FAILED " + url)

for pilot, q in Q.items():
    d_out = os.path.join(OUT, pilot)
    os.makedirs(d_out, exist_ok=True)
    cursor, n, seen, manifest = "*", 0, 0, []
    started = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    while True:
        url = BASE + "?" + urllib.parse.urlencode({"query": q, "format": "json", "resultType": "core", "pageSize": PAGE, "cursorMark": cursor}, quote_via=urllib.parse.quote)
        t = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
        body, d = get(url)
        recs = d["resultList"]["result"]
        n += 1
        fn = f"{pilot}_page{n:03d}.json"
        with open(os.path.join(d_out, fn), "wb") as f:
            f.write(body)
        seen += len(recs)
        manifest.append({"file": f"{pilot}/{fn}", "sha256": hashlib.sha256(body).hexdigest(), "pulled_utc": t,
                         "request_url": url, "cursorMark_in": cursor, "nextCursorMark": d.get("nextCursorMark"),
                         "n_records": len(recs), "hitCount": d.get("hitCount")})
        print(pilot, n, len(recs), seen, d.get("hitCount"), flush=True)
        nxt = d.get("nextCursorMark")
        if not recs or not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(1)
    m = {"pilot": pilot, "query": q, "endpoint": BASE, "params": {"format": "json", "resultType": "core", "pageSize": PAGE},
         "started_utc": started, "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
         "hitCount": manifest[0]["hitCount"], "records_retrieved": seen, "pages": manifest}
    with open(os.path.join(OUT, f"{pilot}_pull_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(m, f, indent=1)
    if seen != m["hitCount"]:
        print(f"WARNING {pilot}: retrieved {seen} != hitCount {m['hitCount']}", file=sys.stderr)
