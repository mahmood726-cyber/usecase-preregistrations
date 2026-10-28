"""P13 documentary build; reads with Python; writes only beneath out/."""
from pathlib import Path
import hashlib, json, re, sys, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
OUT=Path(__file__).resolve().parents[1]
JOB=OUT.parent
SUP=OUT/"supporting"
EV=SUP/"evidence"
V4=JOB/"C_P13_V4/out"
APP=Path(r"allmeta@14dc545/")
SRC=Path(r"sources/")
def read(p): return Path(p).read_text(encoding="utf-8")
def sha(b): return hashlib.sha256(b).hexdigest()
def write(p,t):
    p=Path(p).resolve()
    assert p.is_relative_to(OUT)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(t,encoding="utf-8",newline="\n")
records=[]
def copy(p,rel,origin):
    b=Path(p).read_bytes()
    dst=(EV/rel).resolve()
    assert dst.is_relative_to(EV)
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_bytes(b)
    assert dst.read_bytes()==b
    records.append(dict(path=dst.relative_to(SUP).as_posix(),sha256=sha(b),bytes=len(b),
                        provenance=origin,exact_byte_copy=True))
for n in ["JOB.md","JOB_RULES.md","V5.md","FREEZE_CRITERIA.md","MAHMOOD_DECISIONS.md","COAUTHOR_LOAD.md","PIN.txt","R_ENV.txt"]:
    copy(JOB/n,"instructions/"+n,"Supplied job file: "+n)
for n in ["PREREG_P13_usecase.md","V4_NOTES_P13.md"]:
    copy(V4/n,"history/v4_"+n,"Supplied v4 package: "+n)
for n in ["ANALYSIS_CONTRACT_P13.md","VERIFICATION_P13.md"]:
    copy(V4/"supporting"/n,"history/v4_"+n,"Supplied v4 supporting file: "+n)
copy(JOB/"B_P13_V3/out/SOURCE_CHECK_P13.md","history/v3_SOURCE_CHECK_P13.md","Historical source screen; model conclusions superseded")
for n in ["NOVELTY_pc2_2026-10-28.json","NOVELTY_openalex_2026-10-28.json"]:
    copy(JOB/n,"novelty/"+n,"Supplied full novelty log: "+n)
copy(SRC/"FETCH_LOG.json","FETCH_LOG.json","Supplied full retrieval log")
prior=json.loads(read(V4/"supporting/browser_dependencies_P13.json"))
for role,names in {
 "primary":["fulltext.xml","rkag034.pdf","supplementary.zip","Supplementary_Materials_ACCEPTED.pdf","supp/rkag034f1.jpg","supp/rkag034_supplementary_data.zip"],
 "fallback":["fulltext.xml","supplementary.zip","supp/rkad084f2.jpg","supp/rkad084_supplementary_data.docx"]
}.items():
    for n in names:
        old=next(x for x in prior["source_files"] if x["role"]==role and x["file"]==n)
        p=SRC/("P13_"+role)/n
        assert sha(p.read_bytes())==old["sha256"]
        copy(p,role+"/"+n,old.get("url","Supplied "+role+" supplementary asset: "+n))
assets=[]
for old in prior["assets"]:
    if old["scope"] in ["optional built-in replay; NOT RUN","optional built-in webR"]: continue
    p=APP/old["path"]
    assert old["exists"] and sha(p.read_bytes())==old["sha256"], old["path"]
    copy(p,"app/"+old["path"],"Declared allmeta snapshot; app-relative: "+old["path"])
    assets.append(old)
manifest=dict(date="2026-10-28",stage="pre-release; documentary audit only",
 declared_snapshot=prior["declared_snapshot"],embedded_build_sha=prior["embedded_build_sha"],
 direct_asset_count=prior["direct_asset_count"],direct_missing=[],assets=assets,
 evidence_files=records,novelty_P13_metadata=prior["novelty_logs"],
 limits=["No study-level extraction or analysis","No R/browser runtime validation",
 "Historical exact copies can contain obsolete paths/conclusions; active v5 documents control",
 "No independent novelty record-level rereview; request URLs/full screening lists unavailable",
 "Optional replay corpora/webR are outside this route and were not run"])
write(SUP/"evidence_manifest_P13.json",json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
c=read(V4/"supporting/ANALYSIS_CONTRACT_P13.md").replace("# P13 v4 normative","# P13 v5 normative")
c=c.replace(", locally C:/Users/User/ucjobs/allmeta_14dc545/gosh/index.html"," (archived at [evidence/app/gosh/index.html](evidence/app/gosh/index.html))")
c=c.replace("The original-model branch stays fail-closed until the F3 configuration is fixed; this supplement is not that configuration.","The original-model configuration is fixed in [REPRODUCTION_P13.md](REPRODUCTION_P13.md). Its REML gate precedes this unchanged DL/PFT new analysis. Execution stays closed until release/DOI and all mandatory synthetic and workflow conditions pass.")
write(SUP/"ANALYSIS_CONTRACT_P13.md",c)
v=read(V4/"supporting/VERIFICATION_P13.md").replace("# P13 v4 normative","# P13 v5 normative")
write(SUP/"VERIFICATION_P13.md",v)
print("Archived",len(records),"evidence files and preserved normative contracts.")
