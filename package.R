library(roxygen2)
library(devtools)

setwd("/Users/alice/Documents/R/StatsProgramming_202A")
create("LMjw")

library(Rcpp)
library(RcppArmadillo)
RcppArmadillo.package.skeleton("JWlm",force=T)

setwd("/Users/alice/Documents/R/StatsProgramming_202A/LMjw")
document()
compileAttributes(verbose=TRUE)

setwd("/Users/alice/Documents/R/StatsProgramming_202A")
install("LMjw")

library(Rcpp)
library(RcppArmadillo)
RcppArmadillo.package.skeleton("LMjw")
