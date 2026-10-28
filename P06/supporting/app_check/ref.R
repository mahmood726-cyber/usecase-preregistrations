source(commandArgs(TRUE)[1]); suppressMessages(library(metafor)); library(jsonlite)
cat("metafor", as.character(packageVersion("metafor")), "\n")
r <- regtest(rma(yi,sei=sei,method="FE"), model="lm", predictor="sei", ret.fit=TRUE)
v <- sei^2
pet <- coef(summary(lm(yi ~ sei, weights=1/v))); peese <- coef(summary(lm(yi ~ I(v), weights=1/v)))
q <- qt(.975, 10)
re <- rma(yi,sei=sei,method="REML"); dl <- rma(yi,sei=sei,method="DL")
cat(toJSON(list(egger_t=r$zval, egger_p=r$pval, egger_dfs=r$dfs, egger_limit=r$est,
 pet_b0=pet[1,1], pet_se=pet[1,2], pet_t=pet[1,3], pet_p=pet[1,4], pet_b1=pet[2,1], pet_b1_t=pet[2,3], pet_b1_p=pet[2,4],
 pet_lo=pet[1,1]-q*pet[1,2], pet_hi=pet[1,1]+q*pet[1,2],
 peese_b0=peese[1,1], peese_se=peese[1,2], peese_t=peese[1,3], peese_p=peese[1,4], peese_lo=peese[1,1]-q*peese[1,2], peese_hi=peese[1,1]+q*peese[1,2],
 reml=c(coef(re)), dl=c(coef(dl))), digits=NA, auto_unbox=TRUE), "\n")
