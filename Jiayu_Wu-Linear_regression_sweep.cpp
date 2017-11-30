/*
####################################################
## Stat 202A - Homework 2
## Author: Jiayu Wu
## Date : 10192017
## Description: This script implements linear regression 
## using the sweep operator
####################################################
 
###########################################################
## INSTRUCTIONS: Please fill in the missing lines of code
## only where specified. Do not change function names, 
## function inputs or outputs. MAKE SURE TO COMMENT OUT ALL 
## OF YOUR EXAMPLES BEFORE SUBMITTING.
##
## Very important: Do not change your working directory
## anywhere inside of your code. If you do, I will be unable 
## to grade your work since R will attempt to change my 
## working directory to one that does not exist.
###########################################################
 
 */ 

/* ~~~~~~~~~~~~~~~~~~~~~~~~~ 
Problem 1: Sweep operator 
~~~~~~~~~~~~~~~~~~~~~~~~~ */


# include <RcppArmadillo.h>
// [[Rcpp::depends(RcppArmadillo)]]
using namespace Rcpp;
using namespace arma;


// [[Rcpp::export]]
mat mySweepC(const mat A, int m) {
       
       // Declare our output
       mat B = A;
       int n = B.n_rows;
       
       for (int k=0; k<m; k++) {
              for (int j=0; j<n; j++) {
                     for (int i=0; i<n; i++) {
                            if (i != k & j != k) {
                                   B(i,j) = B(i,j)-B(i,k)*B(k,j)/B(k,k);
                            }
                     }}
              for (int i=0; i<n; i++) {
                     if (i != k) {
                            B(i,k) = B(i,k)/B(k,k);
                     }
              }
              for (int j=0; j<n; j++) {
                     if (j!=k) {
                            B(k,j) = B(k,j)/B(k,k);
                     }      
              } 
              B(k,k) = -1/B(k,k);
       }
       return(B);
}



/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Problem 2: Linear regression using the sweep operator 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */


// [[Rcpp::export()]]
mat myLinearRegressionC(const mat X, const mat Y){
       
       /*  
       Find the regression coefficient estimates beta_hat
       corresponding to the model Y = X * beta + epsilon
       Your code must use the sweep operator you coded above.
       Note: we do not know what beta is. We are only 
       given a matrix X and a matrix Y and we must come 
       up with an estimate beta_hat.
       
       X: an 'n row' by 'p column' matrix of input variables.
       Y: an 'n row' by '1 column' matrix of responses
       
#############################################
## FILL IN THE BODY OF THIS FUNCTION BELOW ##
#############################################
       */  
       
       // Let me start things off for you...
       int n = X.n_rows;
       int p = X.n_cols;
       
       mat O;
       O.ones(n,1);
       mat M = join_rows(O,X);
       mat Z = join_rows(M,Y);
       mat A = Z.t() * Z;
       
       mat S = mySweepC(A,p+1);
       mat beta_hat = S.submat(span(0,p),span(p+1,p+1));
       
       // Function returns the 'p+1' by '1' matrix 
       // beta_hat of regression coefficient estimates
       return(beta_hat);
       
}


/*** R
testing_Linear_Regression <- function(){
       
## Define parameters
       n    <- 100
       p    <- 3
       
## Simulate data from our assumed model.
## We can assume that the true intercept is 0
       X    <- matrix(rnorm(n * p), nrow = n)
       beta <- matrix(1:p, nrow = p)
       Y    <- X %*% beta + rnorm(n)
       
## Save R's linear regression coefficients
       R_coef  <- coef(lm(Y ~ X))
       
## Save our linear regression coefficients
       my_coef <- myLM(X, Y)
       
## Are these two vectors different?
       sum_square_diff <- sum((R_coef - my_coef)^2)
       if(sum_square_diff <= 0.001){
              return('Both results are identical')
       }else{
              return('There seems to be a problem...')
       }
       
}
testing_Linear_Regression()
       */