"""AM-S8 deterministic independence rule (single source; used by second_pass.py and screen.facts_for)."""
import re

# dependence markers only: a single arm/dose-labelled row is still one contrast (repeats are caught by the label check)
ANNOT = re.compile(r"shared control|split control|control (?:group )?(?:was )?(?:split|shared|halved|divided)|common control|same control|half (?:of )?(?:the )?control|multi-?arm", re.I)

def norm_label(lab):
    s = re.sub(r"\[[^\]]*\]|\([^)]*\)", " ", lab or "").lower()  # citation numbers / parenthetical arm notes
    s = re.sub(r"[¹²³⁰-₟]", "", s)          # superscript citation numerals
    m = re.search(r"([a-z][a-z' -]*?)\s*,?\s*(?:et al\.?\s*,?\s*)?((?:19|20)\d{2})", s)
    if m:
        author = re.sub(r"[^a-z]", "", m.group(1).split()[0])
        return f"{author}{m.group(2)}"
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"\b[a-z]\b$", "", s))

def independence(res, k=None):
    """'yes' / 'no' / None (stays unresolved), with a reason.
    'no' needs only one repeated trial or a dependence annotation. 'yes' needs a complete row list:
    one label per designated trial (len(labels) == k_designated); otherwise the rows were not identified."""
    if not res or res.get("source_found") != "yes" or len(res.get("labels") or []) < 2:
        return None, "designated rows not identified"
    labs = res["labels"]
    if any(ANNOT.search(a or "") for a in (res.get("annotations") or [])) or any(ANNOT.search(l) for l in labs):
        return "no", "shared/split-control or multi-arm annotation present"
    normed = [norm_label(l) for l in labs]
    dup = sorted({n for n in normed if normed.count(n) > 1})
    if dup:
        return "no", "repeated normalised label(s): " + ", ".join(dup[:5])
    if k is None or len(labs) != k:
        return None, f"incomplete row list: {len(labs)} labels for k_designated={k}"
    return "yes", f"{len(normed)} unique normalised labels = k_designated"
