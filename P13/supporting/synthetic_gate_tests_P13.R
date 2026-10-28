# SYNTHETIC - not data
# Unexecuted handoff for pc2; this is not the full browser/GOSH validation suite.
args <- commandArgs(trailingOnly=FALSE)
script_arg <- grep("^--file=", args, value=TRUE)
if (length(script_arg) != 1L) stop("Run this script with Rscript on pc2")
script <- normalizePath(sub("^--file=", "", script_arg), mustWork=TRUE)
source(file.path(dirname(script), "original_gate_P13.R"))
p13_runtime_check()
expect_error <- function(expr) {
  failed <- FALSE
  tryCatch(force(expr), error=function(e) failed <<- TRUE)
  if (!failed) stop("Expected refusal")
}
for (candidate in c("primary","fallback")) {
  spec <- p13_target(candidate)
  target <- spec$target
  tol <- spec$tolerance
  stopifnot(p13_gate_components(target,candidate)$pass)
  for (j in seq_len(3L)) for (direction in c(-1,1)) {
    boundary <- target
    boundary[j] <- target[j]+direction*tol
    stopifnot(p13_gate_components(boundary,candidate)$pass)
    beyond <- boundary
    beyond[j] <- beyond[j]+direction*1e-7
    stopifnot(!p13_gate_components(beyond,candidate)$pass)
  }
  synthetic_n <- 80+7*seq_len(spec$k)
  synthetic_x <- floor(synthetic_n*(0.2+0.5*seq_len(spec$k)/(spec$k+1)))
  synthetic_fit <- p13_fit_reproduction(synthetic_x,synthetic_n,candidate)
  if (candidate=="primary") {
    expected_y <- 0.5*(asin(sqrt(synthetic_x/(synthetic_n+1)))+
                       asin(sqrt((synthetic_x+1)/(synthetic_n+1))))
    expected_v <- 1/(4*synthetic_n+2)
    stopifnot(isTRUE(all.equal(synthetic_fit$harmonic_mean_n,
                              length(synthetic_n)/sum(1/synthetic_n),tolerance=1e-14)))
  } else {
    expected_y <- synthetic_x/synthetic_n
    expected_v <- expected_y*(1-expected_y)/synthetic_n
  }
  stopifnot(isTRUE(all.equal(as.numeric(synthetic_fit$yi),expected_y,tolerance=1e-14)),
            isTRUE(all.equal(as.numeric(synthetic_fit$vi),expected_v,tolerance=1e-14)))
  expect_error(p13_fit_reproduction(synthetic_x[-1],synthetic_n[-1],candidate))
  synthetic_bad_x <- synthetic_x
  synthetic_bad_x[1] <- 0.5
  expect_error(p13_fit_reproduction(synthetic_bad_x,synthetic_n,candidate))
  if (candidate=="fallback") {
    synthetic_bad_x[1] <- 0
    expect_error(p13_fit_reproduction(synthetic_bad_x,synthetic_n,candidate))
    synthetic_bad_x[1] <- synthetic_n[1]
    expect_error(p13_fit_reproduction(synthetic_bad_x,synthetic_n,candidate))
  }
}
synthetic_n <- rep(100,17)
synthetic_x <- c(0,100,seq(15,85,length.out=15))
synthetic_fit <- p13_fit_reproduction(synthetic_x,synthetic_n,"primary")
stopifnot(all(is.finite(synthetic_fit$yi)),all(synthetic_fit$vi>0))
expect_error(p13_gate_components(c(NA_real_,0,1),"primary"))
expect_error(p13_gate_components(c(0.5,0.6,0.4),"fallback"))
cat("SYNTHETIC - not data: gate component and model checks passed; not runtime parity.\n")
print(sessionInfo())
