"""Static P12 v4 audit. Reads with Python and writes only under out/.
Source and corpus resources are hashed as opaque bytes, never analysed.
This is not a browser runtime dependency-closure test.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re

WORK = Path(__file__).resolve().parents[2]
OUT = WORK / "out"
ROOT = Path("C:/Users/User/ucjobs/allmeta_14dc545")
SOURCES = Path("C:/Users/User/ucsources")


def record(path):
    if not path.is_file():
        return {"exists": False, "bytes": None, "sha256": None}
    data = path.read_bytes()
    return {"exists": True, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and attrs.get("src"):
            self.refs.append(("script", attrs["src"]))
        if tag == "link" and "stylesheet" in attrs.get("rel", "").split():
            self.refs.append(("stylesheet", attrs["href"]))


entry = ROOT / "limit-ma/index.html"
parser = Links()
parser.feed(entry.read_text(encoding="utf-8"))
resources = []
for kind, href in parser.refs:
    url = urlsplit(href)
    if url.scheme or url.netloc:
        resources.append({"kind": kind, "href": href, "external": True})
        continue
    path = (ROOT / unquote(url.path).lstrip("/")) if url.path.startswith("/") else (entry.parent / unquote(url.path))
    path = path.resolve()
    resources.append({"kind": kind, "href": href, "path": path.relative_to(ROOT).as_posix(), **record(path)})

# Targets identified by reading loaders; optional and excluded routes are distinct.
dynamic = [
    ("hub/shared/glossary.json", "English tooltips; index.html:782; tooltips.js:_loadAndRefresh"),
    ("hub/shared/vendor/jspdf.min.js", "Optional PDF export; plot-export.js:loadPdf; script-relative"),
    ("shared/webr-runner.js", "Optional browser R; alm-validate.js:runner; script-relative"),
    ("r-shiny/shinylive/webr/webr.mjs", "Optional browser R runtime; webr-runner.js:_ensureWebR"),
    ("r-shiny/shinylive/webr/repo/manifest.json", "Optional browser R package manifest; webr-runner.js"),
    ("limit-ma/validate/corpus/corpus.json", "Excluded archived replay; adapter.js:files; bytes only"),
    ("limit-ma/validate/corpus/reference.json", "Excluded archived replay; adapter.js:files; bytes only"),
    ("limit-ma/validate/plus/corpus.json", "Excluded archived replay; plus-pins.js; bytes only"),
    ("limit-ma/validate/plus/reference.json", "Excluded archived replay; plus-pins.js; bytes only"),
]
dynamic_records = [{"path": n, "scope": scope, **record(ROOT / n)} for n, scope in dynamic]
code_records = [{"path": n, **record(ROOT / n)} for n in
                ["limit-ma/index.html", "limit-ma/validate/generate-plus.R", "limit-ma/validate/loo/generate.R"]]
prior = WORK / "B_P12_V3/out"
source_text = (prior / "SOURCE_CHECK_P12.md").read_text(encoding="utf-8")
source_records = []
for name, expected in re.findall(r"\| (P12_(?:primary|fallback)/[^|]+?) \| ([0-9a-f]{64}) \|", source_text):
    current = record(SOURCES / name)
    source_records.append({"path": name, "v3_sha256": expected, **current,
                           "matches_v3": current["sha256"] == expected})
assert len(source_records) == 6

expected_pins = dict(re.findall(r"^\s+(\S+)\s+([0-9a-f]{64})$", (WORK / "PIN.txt").read_text(encoding="utf-8"), re.M))
for item in resources + code_records + dynamic_records:
    if item.get("path") in expected_pins:
        item["PIN_txt_sha256"] = expected_pins[item["path"]]
        item["matches_PIN_txt"] = item.get("sha256") == expected_pins[item["path"]]

inputs = ["JOB.md", "JOB_RULES.md", "V4.md", "FREEZE_CRITERIA.md", "MAHMOOD_DECISIONS.md",
          "COAUTHOR_LOAD.md", "PIN.txt", "R_ENV.txt", "NOVELTY_pc2_2026-10-28.json", "NOVELTY_openalex_2026-10-28.json"]
inputs += ["B_P12_V3/out/" + n for n in
           ["PREREG_P12_usecase.md", "SOURCE_CHECK_P12.md", "CHANGELOG_P12.md", "BLOCKERS_P12.md"]]
novelty = {}
for name in ["NOVELTY_pc2_2026-10-28.json", "NOVELTY_openalex_2026-10-28.json"]:
    novelty[name] = [r for r in json.loads((WORK / name).read_text(encoding="utf-8")) if r["paper"] == "P12"]
build = (ROOT / "shared/build-info.js").read_text(encoding="utf-8")
result = {
    "audit_date": "2026-10-28", "method": "Python static reads and SHA-256; no browser or R execution",
    "app_root": str(ROOT), "job_commit": "14dc545bcba87a02158b2f445c28450e7eaf6b89",
    "embedded_build_commits": sorted(set(re.findall(r"\b[0-9a-f]{40}\b", build))),
    "git_metadata_present": (ROOT / ".git").exists(),
    "direct_resource_count": len(resources),
    "direct_resources_all_present": all(r.get("exists", False) for r in resources),
    "direct_resources": resources, "dynamic_and_excluded_resources": dynamic_records,
    "entry_and_R_reference_code": code_records, "source_hash_checks": source_records,
    "input_files": [{"path": n, **record(WORK / n)} for n in inputs], "novelty_P12": novelty,
    "closure_limit": "Direct links and named loader targets inspected. Runtime closure, optional translations, browser requests, exports and synthetic parity remain untested. No archived corpus executed.",
}
target = OUT / "supporting/DEPENDENCIES_P12.json"
assert target.resolve().is_relative_to(OUT.resolve())
target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({"direct_resources": len(resources),
                  "all_direct_present": result["direct_resources_all_present"],
                  "all_sources_match_v3": all(r["matches_v3"] for r in source_records),
                  "pin_mismatches": [r["path"] for r in resources + code_records + dynamic_records if r.get("matches_PIN_txt") is False],
                  "missing_named_dynamic": [r["path"] for r in dynamic_records if not r["exists"]],
                  "embedded_commits": result["embedded_build_commits"]}, indent=2))
