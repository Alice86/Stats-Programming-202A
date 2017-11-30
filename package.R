## How to make a package in R

# import packages
library(roxygen2)
library(devtools)

# creat the project
setwd("/Users/alice/Documents/R/StatsProgramming_202A")
create("LMjw")
# if the package requires rcpp
library(Rcpp)
library(RcppArmadillo)
RcppArmadillo.package.skeleton("JWlm",force=T)

# edit and save codes

# export functions and generate documents
setwd("/Users/alice/Documents/R/StatsProgramming_202A/LMjw")
document()
compileAttributes(verbose=TRUE)

# install and try
setwd("/Users/alice/Documents/R/StatsProgramming_202A")
install("LMjw")
