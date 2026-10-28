"""Static P08 v4 audit; Python reads and out-only writes. No R/JS execution.
Run from the job directory: python -X utf8 out/supporting/audit_v4.py
Only published pooled summaries are compared; no study inputs are extracted.
"""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out"
APP = Path(r"allmeta@14dc545/")
SOURCES = Path(r"sources/")


def read(path):
    return path.read_text(encoding="utf-8-sig")


def write(path, text):
    path = path.resolve()
    assert path.is_relative_to(OUT.resolve())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def record(path, base):
    item = {"path": path.relative_to(base).as_posix(), "exists": path.is_file()}
    if item["exists"]:
        raw = path.read_bytes()
        item.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    return item


class Assets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and attrs.get("src"):
            self.refs.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.refs.append(attrs["href"])


def main():
    html = read(APP / "meta-regression/index.html")
    parser = Assets()
    parser.feed(html)
    direct = sorted({(APP / "meta-regression" / ref).resolve() for ref in parser.refs})
    assert all(path.is_relative_to(APP.resolve()) for path in direct)
    missing = [str(path) for path in direct if not path.is_file()]
    assert not missing, missing
    optional_names = [
        "hub/shared/glossary.json", "hub/shared/glossary.ar.json",
        "hub/shared/glossary.es.json", "hub/shared/glossary.zh.json",
        "hub/shared/vendor/jspdf.min.js", "shared/webr-runner.js",
        "meta-regression/validate/reference.R", "meta-regression/validate/README-plus.md",
        "meta-regression/validate/plus/corpus.json",
        "meta-regression/validate/plus/reference.json",
        "meta-regression/validate/plus/candidates.json",
        "meta-regression/validate/plus/divergences.json",
        "r-shiny/shinylive/webr/webr.mjs",
        "r-shiny/shinylive/webr/repo/manifest.json",
    ]
    pin = dict(re.findall(r"^  (\S+)  ([0-9a-f]{64})$", read(ROOT / "PIN.txt"), re.M))
    paths = sorted(set([APP / "meta-regression/index.html"] + direct +
                       [APP / name for name in optional_names]))
    records = [record(path, APP) for path in paths]
    for item in records:
        if item["path"] in pin:
            item["matches_PIN_txt"] = item.get("sha256") == pin[item["path"]]
            assert item["matches_PIN_txt"], item["path"]

    source_records = []
    for role in ("primary", "fallback"):
        for path in sorted((SOURCES / ("P08_" + role)).rglob("*")):
            if path.is_file():
                source_records.append(record(path, SOURCES))
    pxml = ET.fromstring((SOURCES / "P08_primary/fulltext.xml").read_bytes())
    fxml = ET.fromstring((SOURCES / "P08_fallback/fulltext.xml").read_bytes())
    ptext = " ".join(pxml.find('.//sec[@id="sec4-3"]').itertext())
    ftext = " ".join(fxml.find('.//sec[@id="sec24"]').itertext())
    assert "2.38 (95%CI 1.93–2.84)" in ptext
    assert "2.92 (95%CI 2.64–3.20)" in ptext
    assert "SMD: −0.34; 95% CI: −0.62, −0.07" in ftext
    assert "Ten studies" in ftext

    # Generate text, never execute it. These functions are private in the page.
    start = html.index("    function lnGamma(")
    end = html.index("    function tQuantile975(", start)
    tail_functions = html[start:end]
    capture = """/* P08 v4 full-precision capture; NOT EXECUTED here.
 * Use only in the validated post-release session, after fitting.
 * lnGamma/betaCF/betaInc/tTwoSidedP below are verbatim pinned page text.
 * This helper never fits a model or substitutes R output.
 */
(function () {
  'use strict';
""" + tail_functions + """
  window.P08Capture = Object.freeze({
    primary: function () {
      return window.AlmMetaPlusUI.exportPayload();
    },
    fallback: function () {
      const out = structuredClone(window.__almResults());
      const studies = window._almLastStudies();
      if (out.k !== 10 || studies.length !== 10) throw Error('Expected ten accepted rows');
      const t = out.slope / out.slope_se;
      out.slope_t = t;
      out.slope_p = tTwoSidedP(Math.abs(t), out.hksj_q_df);
      for (const key of ['intercept', 'intercept_se', 'intercept_ci_lb',
                        'intercept_ci_ub', 'slope', 'slope_se', 'slope_ci_lb',
                        'slope_ci_ub', 'tau2_pm', 'hksj_q', 'hksj_q_df',
                        'slope_t', 'slope_p']) {
        if (!Number.isFinite(out[key])) throw Error('Nonfinite browser output: ' + key);
      }
      return {result: out, accepted: structuredClone(studies)};
    }
  });
})();
"""
    write(OUT / "supporting/capture_app_P08.js", capture)

    prereg = read(OUT / "PREREG_P08_usecase.md")
    binding = next(line[3:] for line in read(ROOT / "MAHMOOD_DECISIONS.md").splitlines()
                   if line.startswith("4. Human verification:"))
    assert binding in prereg, "Binding item 4 is not verbatim"
    old = read(ROOT / "B_P08_V3/out/PREREG_P08_usecase.md")
    old_def = old.split("## 7. New versus robust\n", 1)[1].split("## 8.", 1)[0].strip()
    new_def = prereg.split("## 7. New versus robust\n", 1)[1].split("## 8.", 1)[0].strip()
    assert old_def == new_def, "Changed new-versus-robust definitions"
    count = len(prereg.split())
    assert count <= 3000, count
    assert read(OUT / "BLOCKERS_P08.md") == "NONE\n"
    assert "Mandatory post-release, pre-analysis conditions" in prereg
    for target in re.findall(r"\]\((supporting/[^)#]+)(?:#[^)]*)?\)", prereg):
        if target != "supporting/FILE_HASHES_P08.json":
            assert (OUT / target).is_file(), target
    # FILE_HASHES is created below; link existence for it is checked after write.
    checks = {
        "prereg_word_count": count,
        "word_count_method": "Python len(text.split()); includes headings/tables/code",
        "published_pooled_values": "PASS: direct XML assertions and visual summary check",
        "direct_asset_presence": "PASS",
        "binding_verification": "PASS: verbatim MAHMOOD_DECISIONS item 4",
        "outcome_definitions": "PASS: verbatim v3 section 7",
        "clinical_data_analysis": "NOT RUN",
        "R_JS_runtime_validation": "NOT RUN",
    }
    inputs = [ROOT / name for name in [
        "JOB.md", "JOB_RULES.md", "V4.md", "FREEZE_CRITERIA.md",
        "MAHMOOD_DECISIONS.md", "COAUTHOR_LOAD.md", "PIN.txt",
        "NOVELTY_pc2_2026-10-28.json", "NOVELTY_openalex_2026-10-28.json"]]
    kit = Path(r"job-workdir/out")
    payload = {
        "stage": "pre-release; static inspection only", "date": "2026-10-28",
        "allmeta_commit": "14dc545bcba87a02158b2f445c28450e7eaf6b89",
        "allmeta_root": str(APP), "source_root": str(SOURCES),
        "direct_script_stylesheet_references": len(parser.refs),
        "direct_unique_files": len(direct), "app_files": records,
        "sources": source_records,
        "job_inputs": [record(path, ROOT) for path in inputs],
        "legacy_kit_files": [record(path, kit) for path in sorted(kit.glob("*"))
                             if path.is_file() and path.name != ".keep"],
        "checks": checks,
        "outputs": [record(path, OUT) for path in sorted(OUT.rglob("*"))
                    if path.is_file() and path.name not in (".keep", "FILE_HASHES_P08.json")],
        "scope_limit": "Static presence is not browser closure. Optional live webR missing. No release timestamp claimed. Manifest omits its own hash."
    }
    write(OUT / "supporting/FILE_HASHES_P08.json",
          json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"checks": checks, "direct_assets": len(direct),
                      "missing_optional": [x["path"] for x in records if not x["exists"]]},
                     indent=2))


if __name__ == "__main__":
    main()
