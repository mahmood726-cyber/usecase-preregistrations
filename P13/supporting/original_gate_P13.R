# P13 v5: fixed prospective reproduction. No data are loaded or run on sourcing.
# Real-data use requires release/DOI and all preregistered synthetic/workflow gates.

p13_runtime_check <- function() {
  if (getRversion() != package_version("4.6.0")) stop("R 4.6.0 required")
  if (!requireNamespace("metafor", quietly=TRUE)) stop("metafor required")
  if (utils::packageVersion("metafor") != package_version("5.2.1"))
    stop("metafor 5.2.1 required")
  invisible(TRUE)
}

p13_target <- function(candidate) {
  if (identical(candidate, "primary"))
    return(list(k=17L, target=c(estimate=64, lower=51, upper=76), tolerance=0.5))
  if (identical(candidate, "fallback"))
    return(list(k=30L, target=c(estimate=0.56, lower=0.49, upper=0.63), tolerance=0.005))
  stop("candidate must be exactly primary or fallback")
}

p13_gate_components <- function(observed, candidate) {
  spec <- p13_target(candidate)
  if (!is.numeric(observed) || length(observed) != 3L ||
      any(!is.finite(observed))) stop("Three finite outputs required")
  if (observed[2] > observed[1] || observed[1] > observed[3])
    stop("Invalid estimate/CI ordering")
  names(observed) <- names(spec$target)
  passed <- observed >= spec$target-spec$tolerance &
            observed <= spec$target+spec$tolerance
  list(pass=all(passed), components=passed, observed=observed,
       published_target=spec$target, tolerance=spec$tolerance,
       absolute_difference=abs(observed-spec$target))
}

p13_fit_reproduction <- function(x, n, candidate) {
  p13_runtime_check()
  spec <- p13_target(candidate)
  if (!is.numeric(x) || !is.numeric(n) || length(x) != spec$k ||
      length(n) != spec$k || any(!is.finite(c(x,n))) ||
      any(n <= 0 | n != floor(n) | x != floor(x) | x < 0 | x > n))
    stop("Invalid or incomplete printed-count inventory; no omission permitted")
  # Identity, provenance, independence and release authorization are external
  # mandatory checks; this numerical function cannot certify them.
  old_options <- options(na.action="na.fail")
  on.exit(options(old_options), add=TRUE)
  withCallingHandlers({
    measure <- if (identical(candidate,"primary")) "PFT" else "PR"
    es <- metafor::escalc(measure=measure, xi=x, ni=n, vtype="LS",
                          add=0, to="none", drop00=FALSE, append=FALSE)
    if (length(es$yi) != spec$k || any(!is.finite(c(es$yi,es$vi))) ||
        any(es$vi <= 0)) stop("Invalid variance/effect; no correction or deletion")
    fit <- metafor::rma(yi=es$yi, vi=es$vi, method="REML",
                       test="z", level=95, weighted=TRUE, intercept=TRUE,
                       control=list(tau2.init=NULL, tau2.min=0,
                                    threshold=1e-5, maxiter=100L, stepadj=1))
    if (fit$k != spec$k) stop("Fit inventory changed")
    model_output <- c(estimate=as.numeric(stats::coef(fit)),
                      lower=as.numeric(fit$ci.lb), upper=as.numeric(fit$ci.ub))
    if (length(model_output) != 3L || any(!is.finite(model_output)))
      stop("Invalid fitted output")
    harmonic_n <- NA_real_
    if (identical(candidate,"primary")) {
      harmonic_n <- length(n)/sum(1/n)
      observed <- 100*metafor::transf.ipft.hm(model_output, targs=list(ni=n))
    } else {
      observed <- model_output
    }
    gate <- p13_gate_components(observed,candidate)
    list(candidate=candidate, measure=measure, yi=es$yi, vi=es$vi,
         tau2=fit$tau2, model_output=model_output, harmonic_mean_n=harmonic_n,
         gate=gate, configuration="P13-v5-REML-z-95",
         R=as.character(getRversion()),
         metafor=as.character(utils::packageVersion("metafor")))
  }, warning=function(w) stop(paste("Fixed configuration warning:",conditionMessage(w)),
                             call.=FALSE))
}
