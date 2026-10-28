"""P13 v5 documentary audit only. No study-row extraction or statistical execution."""
from pathlib import Path
from xml.etree import ElementTree as E
import ast, hashlib, io, json, re, sys, zipfile
sys.stdout.reconfigure(encoding="utf-8")
SUP=Path(__file__).resolve().parent
OUT=SUP.parent
EV=SUP/"evidence"
def read(p): return Path(p).read_text(encoding="utf-8")
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write_json(p,data):
    assert p.resolve().is_relative_to(OUT)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
manifest=json.loads(read(SUP/"evidence_manifest_P13.json"))
bad_hashes=[]
for row in manifest["evidence_files"]:
    p=SUP/row["path"]
    if not p.is_file() or sha(p)!=row["sha256"] or p.stat().st_size!=row["bytes"]:
        bad_hashes.append(row["path"])
terms=["freeman","tukey","transform","arcsin","logit","logarithm","probit","metafor","metaprop","RStudio","Stata","RevMan","SPSS","software","package"]
screen=dict(stage="pre-release screening; no study rows transcribed",method="Keyword search, Methods/caption scope and supplementary structure; not a statistical analysis",files=[])
def screen_text(text,rel,extra=None):
    result=dict(path=rel,keyword_counts={t:len(re.findall(t,text,re.I)) for t in terms})
    if extra: result.update(extra)
    screen["files"].append(result)
for role in ["primary","fallback"]:
    p=EV/role/"fulltext.xml"
    root=E.fromstring(p.read_bytes())
    screen_text(" ".join(root.itertext()),p.relative_to(SUP).as_posix())
def screen_docx(blob,rel):
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        root=E.fromstring(z.read("word/document.xml"))
        drawing_count=sum(1 for e in root.iter() if e.tag.rsplit("}",1)[-1] in ("drawing","pict"))
        screen_text(" ".join(root.itertext()),rel,dict(drawing_elements=drawing_count,
                    embedded_media_count=sum(n.startswith("word/media/") for n in z.namelist())))
p=EV/"fallback/supp/rkad084_supplementary_data.docx"
screen_docx(p.read_bytes(),p.relative_to(SUP).as_posix())
p=EV/"primary/supp/rkag034_supplementary_data.zip"
with zipfile.ZipFile(p) as z:
    for name in z.namelist():
        if name.lower().endswith(".docx"):
            screen_docx(z.read(name),p.relative_to(SUP).as_posix()+"::"+name)
import pypdf
for name in ["rkag034.pdf","Supplementary_Materials_ACCEPTED.pdf"]:
    p=EV/"primary"/name
    pdf=pypdf.PdfReader(p)
    screen_text("\n".join(page.extract_text() or "" for page in pdf.pages),
                p.relative_to(SUP).as_posix(),dict(pages=len(pdf.pages)))
fallback_rows=[x for x in screen["files"] if x["path"].startswith("evidence/fallback/")]
screen["Tang_transformation_not_stated"]=all(
    all(x["keyword_counts"][t]==0 for t in ["freeman","tukey","transform","arcsin","logit","logarithm","probit","metafor","metaprop"])
    for x in fallback_rows)
screen["no_study_fields_emitted"]=True
write_json(SUP/"source_screen_P13.json",screen)
p=read(OUT/"PREREG_P13_usecase.md")
decisions=read(EV/"instructions/MAHMOOD_DECISIONS.md")
binding=next(line[3:] for line in decisions.splitlines() if line.startswith("4. Human verification:"))
old_c=read(EV/"history/v4_ANALYSIS_CONTRACT_P13.md")
new_c=read(SUP/"ANALYSIS_CONTRACT_P13.md")
expected_c=old_c.replace("# P13 v4 normative","# P13 v5 normative")
expected_c=expected_c.replace(", locally C:/Users/User/ucjobs/allmeta_14dc545/gosh/index.html"," (archived at [evidence/app/gosh/index.html](evidence/app/gosh/index.html))")
expected_c=expected_c.replace("The original-model branch stays fail-closed until the F3 configuration is fixed; this supplement is not that configuration.","The original-model configuration is fixed in [REPRODUCTION_P13.md](REPRODUCTION_P13.md). Its REML gate precedes this unchanged DL/PFT new analysis. Execution stays closed until release/DOI and all mandatory synthetic and workflow conditions pass.")
old_v=read(EV/"history/v4_VERIFICATION_P13.md")
new_v=read(SUP/"VERIFICATION_P13.md")
old_p=read(EV/"history/v4_PREREG_P13_usecase.md")
def section(text,start,end): return text.split(start,1)[1].split(end,1)[0]
active_md=sorted(p for p in OUT.rglob("*.md") if not p.is_relative_to(EV))
bad_links=[]
external_links=[]
node_paths=[]
for file in active_md:
    txt=read(file)
    if re.search(r"[A-Za-z]:[/\\]",txt): node_paths.append(file.relative_to(OUT).as_posix())
    for target in re.findall(r"\]\(([^)]+)\)",txt):
        if re.match(r"^[a-zA-Z]+://",target): external_links.append([file.relative_to(OUT).as_posix(),target]); continue
        local=target.split("#",1)[0]
        if local and not (file.parent/local).exists(): bad_links.append([file.relative_to(OUT).as_posix(),local])
syntax_errors=[]
for file in SUP.glob("*.py"):
    try: ast.parse(read(file),filename=str(file))
    except SyntaxError as e: syntax_errors.append([file.name,str(e)])
pin=read(EV/"instructions/PIN.txt")
core_pin_checks=[]
for name in ["index.html","exact-enum.js","exact-ui.js","plus.js"]:
    rel="gosh/"+name
    found=re.search(re.escape(rel)+r"\s+([0-9a-f]{64})",pin)
    core_pin_checks.append(bool(found and found[1]==sha(EV/"app"/rel)))
repro=read(SUP/"REPRODUCTION_P13.md")
r=read(SUP/"original_gate_P13.R")
checks={
 "within_3000_words":len(p.split())<=3000,
 "mahmood_item_4_exact_copy":("> "+binding) in p,
 "analysis_contract_preserved_except_declared_status_and_relative_path":new_c==expected_c,
 "verification_preserved_except_version_header":new_v==old_v.replace("# P13 v4 normative","# P13 v5 normative"),
 "main_new_analysis_verbatim":section(p,"## 6. Exact new analysis","## 7. New versus robust")==section(old_p,"## 6. Exact new analysis","## 7. New versus robust"),
 "main_new_versus_robust_verbatim":section(p,"## 7. New versus robust","## 8. Novelty")==section(old_p,"## 7. New versus robust","## 8. Novelty"),
 "evidence_hashes_match":not bad_hashes,
 "all_four_core_app_pins_match":all(core_pin_checks),
 "relative_active_citations_resolve":not bad_links and not external_links and not node_paths,
 "Tang_transform_screen_negative":screen["Tang_transformation_not_stated"],
 "primary_inverse_named_exactly":"transf.ipft.hm using the harmonic mean of n" in p and "transf.ipft.hm" in r,
 "fixed_REML_z_95":all(t in r for t in ['method="REML"','test="z"','level=95']),
 "no_model_search_and_stop_rule":"No model search" in repro and "independently" in p,
 "python_syntax_valid":not syntax_errors,
 "blockers_exact_NONE":(OUT/"BLOCKERS_P13.md").read_bytes()==b"NONE\n",
 "synthetic_R_first_line_marked":read(SUP/"synthetic_gate_tests_P13.R").splitlines()[0]=="# SYNTHETIC - not data",
 "mandatory_post_release_conditions_retained":"## Mandatory post-release, pre-analysis conditions" in p,
}
files=[dict(path=f.relative_to(OUT).as_posix(),sha256=sha(f),bytes=f.stat().st_size)
       for f in sorted(OUT.rglob("*")) if f.is_file() and f.name not in (".keep","VALIDATION_P13.json")]
report=dict(stage="document/byte audit only",prereg_word_count=len(p.split()),
 word_count_method="Python len(text.split()), including headings/tables/link markup",
 checks=checks,all_document_checks_pass=all(checks.values()),
 bad_hashes=bad_hashes,bad_links=bad_links,external_active_links=external_links,
 active_node_paths=node_paths,python_syntax_errors=syntax_errors,
 evidence_file_count=len(manifest["evidence_files"]),registered_analysis_executed=False,
 R_scripts_executed=False,browser_executed=False,source_study_rows_extracted=False,
 REDTEAM2_status="not supplied; follows this job per JOB.md",files=files)
write_json(SUP/"VALIDATION_P13.json",report)
print(json.dumps({k:v for k,v in report.items() if k!="files"},ensure_ascii=False,indent=2))
if not report["all_document_checks_pass"]: raise SystemExit(1)
