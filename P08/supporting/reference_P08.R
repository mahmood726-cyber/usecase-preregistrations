# P08 v4 fixed R reference component; no input data; NOT EXECUTED on this node.
# Sourcing defines functions only. pc2 must validate on synthetic_* fixtures first.
# Do not execute a real-data reproduction gate until the P08 release, DOI,
# aligned kit, source verification and synthetic validation conditions are met.
# This is not the complete orchestration/deletion/verification harness.

p08_environment <- function() {
  stopifnot(as.character(getRversion()) == "4.6.0")
  stopifnot(as.character(utils::packageVersion("metafor")) == "5.2.1")
  invisible(TRUE)
}

p08_z975 <- 1.959963984540054

p08_control <- function(y) {
  list(threshold=1e-12 * max(1, stats::var(y)), stepadj=0.5, maxiter=10000)
}

p08_intervals <- function(d, ratio=FALSE) {
  need <- c("row_key", "estimate", "lower", "upper")
  if (!all(need %in% names(d))) stop("Missing required input columns")
  if (nrow(d) < 2L || anyNA(d$row_key) || any(!nzchar(d$row_key)) ||
      anyDuplicated(d$row_key)) stop("Invalid immutable row keys/count")
  x <- unlist(d[c("estimate", "lower", "upper")], use.names=FALSE)
  if (!is.numeric(x) || any(!is.finite(x))) stop("Nonfinite/nonnumeric intervals")
  if (any(d$lower > d$estimate | d$estimate > d$upper | d$lower >= d$upper))
    stop("Invalid ordered CI")
  if (ratio && any(x <= 0)) stop("Ratio inputs must be positive")
  invisible(TRUE)
}

p08_rma <- function(...) {
  # A numerical warning is a refusal requiring synthetic investigation,
  # never a reason to silently change controls or model.
  withCallingHandlers(metafor::rma(...),
                      warning=function(w) stop(conditionMessage(w), call.=FALSE))
}

p08_triple <- function(m) {
  unname(c(as.numeric(m$b)[1], m$ci.lb[1], m$ci.ub[1]))
}

p08_reproduce <- function(role, panels, source_mapping_cleared) {
  p08_environment()
  if (!isTRUE(source_mapping_cleared)) stop("Source membership/mapping unresolved")
  if (!role %in% c("primary", "fallback")) stop("Unknown candidate")
  required <- if (role == "primary") c("HR", "OR") else "CRP"
  if (!identical(names(panels), required)) stop("Wrong original panel membership")
  targets <- if (role == "primary")
    list(HR=c(2.38, 1.93, 2.84), OR=c(2.92, 2.64, 3.20)) else
    list(CRP=c(-0.34, -0.62, -0.07))
  fitted <- lapply(required, function(nm) {
    d <- panels[[nm]]
    p08_intervals(d, ratio=role == "primary")
    if (role == "fallback" && nrow(d) != 10L) stop("Need all ten CRP studies")
    y <- d$estimate
    v <- ((d$upper-d$lower)/(2*p08_z975))^2
    if (any(!is.finite(v) | v <= 0)) stop("Invalid variance")
    m <- p08_rma(yi=y, vi=v, method=if (role == "primary") "REML" else "DL",
                 test="z", level=95, intercept=TRUE, weighted=TRUE,
                 control=if (role == "primary") p08_control(y) else list())
    actual <- p08_triple(m)
    list(fit=m, target=targets[[nm]], actual=actual,
         passed=all(is.finite(actual)) && all(abs(actual-targets[[nm]]) <= 0.005))
  })
  names(fitted) <- required
  list(role=role, panels=panels, fitted=fitted,
       passed=all(vapply(fitted, function(x) x$passed, logical(1))),
       configuration=if (role == "primary") "V4-natural-REML-z" else "V4-SMD-DL-z")
}

p08_require_gate <- function(gate, role) {
  if (!identical(gate$role, role) || !isTRUE(gate$passed))
    stop("Original-summary reproduction has not passed")
  expected <- if (role == "primary") "V4-natural-REML-z" else "V4-SMD-DL-z"
  if (!identical(gate$configuration, expected)) stop("Wrong reproduction configuration")
}

p08_same_inputs <- function(d, originals) {
  # Gate panels may contain overlapping cohorts, but row keys stay panel-specific.
  old <- do.call(rbind, originals)
  i <- match(d$row_key, old$row_key)
  if (anyNA(i)) stop("New-regression row outside reproduced panel membership")
  for (nm in c("estimate", "lower", "upper")) {
    if (!identical(as.numeric(d[[nm]]), as.numeric(old[[nm]][i])))
      stop("Inputs changed since reproduction")
  }
}

p08_primary_fits <- function(d) {
  # Used unchanged for the full fit and deletion fits; no k/category re-gating here.
  y <- log(d$estimate)
  v <- ((log(d$upper)-log(d$lower))/(2*p08_z975))^2
  D <- d$DM/10
  S <- d$S
  ctl <- p08_control(y)
  reduced <- p08_rma(yi=y, vi=v, mods=~D, method="ML", test="z",
                    level=95, weighted=TRUE, control=ctl)
  full <- p08_rma(yi=y, vi=v, mods=~D+S, method="ML", test="z",
                 level=95, weighted=TRUE, control=ctl)
  a <- anova(reduced, full)
  list(reduced=reduced, full=full,
       comparison=list(LRT=unname(a$LRT), df=full$p-reduced$p, pval=unname(a$pval)))
}

p08_primary <- function(d, gate, independence_and_selection_cleared) {
  p08_environment()
  p08_require_gate(gate, "primary")
  if (!isTRUE(independence_and_selection_cleared))
    stop("Independent cohort/HR preference/assessment mapping unresolved")
  p08_intervals(d, ratio=TRUE)
  p08_same_inputs(d, gate$panels)
  if (!all(c("DM", "S") %in% names(d)) ||
      !is.numeric(d$DM) || !is.numeric(d$S) ||
      any(!is.finite(c(d$DM,d$S)))) stop("Incomplete/nonfinite moderators")
  if (nrow(d) < 10L || nrow(d) > 60L) stop("Primary complete-case k gate")
  if (any(d$DM < 0 | d$DM > 100) || any(!d$S %in% c(0,1)))
    stop("Invalid percentage or known-setting coding")
  for (s in c(0,1)) {
    if (sum(d$S == s) < 5L || length(unique(d$DM[d$S == s])) < 2L)
      stop("Setting count/within-setting variation gate")
  }
  X <- cbind(1, d$DM/10, d$S)
  if (qr(X)$rank != 3L) stop("Rank-deficient design")
  p08_primary_fits(d)
}

p08_fallback_fit <- function(d) {
  y <- d$estimate
  v <- ((d$upper-d$lower)/(2*p08_z975))^2
  duration_months <- d$duration_months
  p08_rma(yi=y, vi=v, mods=~duration_months, method="PM", test="adhoc",
          level=95, weighted=TRUE, control=list(tol=1e-12))
}

p08_fallback <- function(d, gate, activation_and_mapping_cleared) {
  p08_environment()
  p08_require_gate(gate, "fallback")
  if (!isTRUE(activation_and_mapping_cleared))
    stop("Fallback feasibility/novelty/profile/independence/duration not cleared")
  p08_intervals(d)
  p08_same_inputs(d, gate$panels)
  if (nrow(d) != 10L) stop("Need all ten independent CRP studies")
  if (!is.numeric(d$duration_months) || any(!is.finite(d$duration_months)) ||
      length(unique(d$duration_months)) < 2L || any(d$duration_months <= 0))
    stop("Invalid/constant treatment duration")
  p08_fallback_fit(d)
}

p08_class_primary <- function(reduced, full) {
  br <- as.numeric(reduced$b)[2]
  bf <- as.numeric(full$b)[2]
  x <- c(br, bf, reduced$ci.lb[2], reduced$ci.ub[2], full$ci.lb[2], full$ci.ub[2])
  if (any(!is.finite(x))) stop("Nonfinite classification inputs")
  if (abs(br) < 0.01) return("inconclusive")
  if (br*bf < 0 || abs(bf) <= 0.5*abs(br)) return("new")
  if (br > 0 && bf > 0 && reduced$ci.lb[2] > 0 && full$ci.lb[2] > 0 &&
      abs(bf-br)/abs(br) <= 0.20) return("robust")
  "inconclusive/intermediate"
}

p08_class_fallback <- function(m) {
  lo <- m$ci.lb[2]; hi <- m$ci.ub[2]
  if (any(!is.finite(c(lo,hi)))) stop("Nonfinite classification inputs")
  if (hi < 0) return("robust")
  if (lo > 0) return("new, directionally contrasting")
  "inconclusive"
}

p08_values <- function(m) {
  list(k=unname(m$k), p=unname(m$p), beta=as.numeric(m$b), se=as.numeric(m$se),
       statistic=as.numeric(m$zval), pval=as.numeric(m$pval),
       ciLo=as.numeric(m$ci.lb), ciHi=as.numeric(m$ci.ub), tau2=unname(m$tau2),
       logLik=as.numeric(logLik(m)), AIC=unname(AIC(m)), BIC=unname(BIC(m)))
}

p08_numeric_agreement <- function(app, ref, pvalue=FALSE) {
  if (!is.numeric(app) || !is.numeric(ref) || length(app) != length(ref) ||
      !length(ref) || any(!is.finite(c(app,ref)))) stop("Invalid comparison outputs")
  tolerance <- if (pvalue) rep(1e-6, length(ref)) else 1e-8*pmax(1,abs(ref))
  if (any(abs(app-ref) > tolerance)) stop("App/R numerical agreement failed")
  invisible(TRUE)
}

# The runner must additionally enforce exact row identity/order, terms, counts and
# classifications; compare all prereg targets (not rounded cards); and log both
# implementations. For deletion diagnostics call p08_primary_fits or
# p08_fallback_fit on each row deletion, without the original full-data eligibility
# gates. Keep the original full-fit SE reference and include all fitting failures.
# Use VERIFICATION_P08.md for weight union, all extrema ties, exact hash sample,
# unresolved excluded fields, >2% escalation and packet rules.
# Never use a failing synthetic test or a real-data gate to select another model.
