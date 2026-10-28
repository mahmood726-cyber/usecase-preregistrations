"""Deterministic eligibility decision from screening facts (stage C facts, optional stage D image facts).
Applies the draft rules plus pre-freeze amendments A1-A5 identically to every record.
Returns (status, code, note); status in ELIGIBLE, EXCLUDE, UNRESOLVED, PENDING_D."""
import re

REVMAN5 = re.compile(r"(review\s*manager|revman)[^0-9]{0,40}5(\.\d+)?\b", re.I)

def model_status(f, d=None):
    fr, w, tau, ci = f["model_fixed_random"], f["model_weighting"], f["model_tau2"], f["model_ci"]
    sw = (f.get("model_software") or "") + " " + (f.get("model_quote") or "")
    em = f["model_effect_measure"]
    if d:  # a forest-plot label read in stage D refines an unstated/conditional text description
        if fr in ("both", "unclear") or f.get("model_conditional") == "yes":
            if d.get("plot_fixed_random") in ("fixed", "random"): fr = d["plot_fixed_random"]
        if w == "unstated" and d.get("plot_weighting") in ("inverse_variance", "mantel_haenszel", "peto"):
            w = d["plot_weighting"]
        if d.get("plot_weighting") in ("mantel_haenszel", "peto") and w == "inverse_variance":
            return "UNRESOLVED", "MODEL_CONFLICT", "text says IV but plot label says " + d["plot_weighting"]
    if ci == "other":
        return "EXCLUDE", "MODEL_UNSUPPORTED", "CI method other than Wald/HKSJ"
    if fr in ("both", "unclear") or (f.get("model_conditional") == "yes" and fr not in ("fixed", "random")):
        return "PENDING", "MODEL_LABEL", "fixed/random for designated synthesis not stated in text"
    if w in ("mantel_haenszel", "peto", "other"):
        return "EXCLUDE", "MODEL_UNSUPPORTED", f"weighting={w}"
    if fr == "fixed":
        if w == "inverse_variance" or em in ("MD", "SMD"):
            return "OK", "", "IV fixed effect"
        return "PENDING", "MODEL_LABEL", "fixed effect, weighting unstated for ratio/RD measure"
    # random
    if tau in ("PM", "other"):
        return "EXCLUDE", "MODEL_UNSUPPORTED", f"tau2={tau}"
    if tau in ("DL", "REML"):
        return "OK", "", f"IV random {tau}, CI {ci if ci != 'unstated' else 'wald (A3)'}"
    if REVMAN5.search(sw):
        if w in ("inverse_variance", "unstated"):
            if w == "unstated" and em not in ("MD", "SMD") and not d:
                return "PENDING", "MODEL_LABEL", "RevMan 5 random, weighting unstated for ratio measure"
            return "OK", "", "RevMan 5.x random effects = DL, Wald (A3)"
    return "EXCLUDE", "MODEL_UNIDENTIFIABLE", "random effects, tau2 estimator not stated and no RevMan 5.x"

def decide(pilot, f, d=None):
    if f["design_ok"] == "no": return "EXCLUDE", "DESIGN", f["design_note"]
    if f["design_ok"] == "unclear": return "UNRESOLVED", "DESIGN", f["design_note"]
    if f["population_ok"] == "no": return "EXCLUDE", "POPULATION", f["population_note"]
    if f["population_ok"] == "unclear": return "UNRESOLVED", "POPULATION", f["population_note"]
    k = f["k_designated"]
    if d and d.get("trial_rows") is not None and k is not None and d["trial_rows"] != k:
        return "UNRESOLVED", "K_CONFLICT", f"text k={k}, plot rows={d['trial_rows']}"
    if k is None: return "EXCLUDE", "K_UNDETERMINABLE", f["k_source"]
    if not (10 <= k <= 60): return "EXCLUDE", "K_OUT_OF_RANGE", f"k={k}"
    if f["independence_ok"] == "no": return "EXCLUDE", "NONINDEPENDENT", f["independence_note"]
    if f["independence_ok"] == "unclear": return "UNRESOLVED", "NONINDEPENDENT", f["independence_note"]
    ps = f["per_study_data"]
    if ps == "NONE": return "EXCLUDE", "NO_PER_STUDY_DATA", f["per_study_location"]
    if f["pooled_reported"] == "no": return "EXCLUDE", "NO_POOLED_RESULT", ""
    ms, mc, mn = model_status(f, d)
    if ms in ("EXCLUDE", "UNRESOLVED"): return ms, mc, mn
    if pilot == "P14":
        a, b = f["trial_years_min"], f["trial_years_max"]
        if a is None or b is None: return "EXCLUDE", "CHRONOLOGY", "trial years not determinable"
        if b - a < 5: return "EXCLUDE", "CHRONOLOGY", f"span {a}-{b}"
        if f["participants_per_trial_available"] != "yes": return "EXCLUDE", "PARTICIPANTS_MISSING", ""
    need_d = ps in ("FIGURE", "SUPPLEMENT_ONLY") or ms == "PENDING"
    if need_d and d is None:
        return "PENDING_D", "PENDING_D", f"per_study={ps}; model={mc or 'ok'}"
    if d is not None and ps in ("FIGURE", "SUPPLEMENT_ONLY"):  # TABLE data are read from text; D then only supplies a model label
        if d.get("source_found") != "yes":
            return "UNRESOLVED", "PER_STUDY_SOURCE_NOT_READ", d.get("note", "")
        if d.get("per_study_printed") == "no":
            return "EXCLUDE", "NO_PER_STUDY_DATA", d.get("note", "")
        if d.get("per_study_printed") != "yes":
            return "UNRESOLVED", "PER_STUDY_UNCLEAR", d.get("note", "")
    if d is not None and ms == "PENDING":
        return "EXCLUDE", "MODEL_UNIDENTIFIABLE", "plot label did not identify the model: " + d.get("plot_model_label", "")
    return "ELIGIBLE", "NONE", mn
