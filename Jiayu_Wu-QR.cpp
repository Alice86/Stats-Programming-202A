/*
#########################################################
## Stat 202A - Homework 3
## Author: Jiayu Wu
## Date: 10262017
## Description: This script implements QR decomposition,
## linear regression, and eigen decomposition / PCA 
## based on QR.
#########################################################
 
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


# include <RcppArmadillo.h>
// [[Rcpp::depends(RcppArmadillo)]]
using namespace Rcpp;
using namespace arma;


/* ~~~~~~~~~~~~~~~~~~~~~~~~~ 
Sign function for later use 
~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

// [[Rcpp::export()]]
double signC(double d){
       return d<0?-1:d>0? 1:0;
}



/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Problem 1: QR decomposition 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */  


// [[Rcpp::export()]]
List myQRC(const mat A){ 
       
       /*
       Perform QR decomposition on the matrix A
       Input: 
       A, an n x m matrix (mat)
       
#############################################
## FILL IN THE BODY OF THIS FUNCTION BELOW ##
#############################################
       
       */ 
       List output;
       
       int n = A.n_rows;
       int m = A.n_cols;
       mat R = A;
       mat Q = eye<mat>(n,n);
       for (int i=0; i<m-1; i++) {
              mat X;
              X.zeros(n,1);
              X(span(i,n-1),0) = R(span(i,n-1),i);
              mat V = X;
              double x = X(i,0);
              double sign = signC(x);
              double nrm = norm(X);
              V(i,0) = x+sign*nrm;
              double nrmv = norm(V);
              mat U = V/nrmv;
              R -= 2 * U * U.t() * R;
              Q -= 2 * U * U.t() * Q;
       }
       
       
       // Function should output a List 'output', with 
       // Q.transpose and R
       // Q is an orthogonal n x n matrix
       // R is an upper triangular n x m matrix
       // Q and R satisfy the equation: A = Q %*% R
       output["Q"] = Q.t();
       output["R"] = R;
       return(output);
       
}

/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Problem 2: Linear regression using QR 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */


// [[Rcpp::export()]]
mat myLinearRegressionC(const mat X, const mat Y){
       
       /*  
       Perform the linear regression of Y on X
       Input: 
       X is an n x p matrix of explanatory variables
       Y is an n dimensional vector of responses
       Do NOT simulate data in this function. n and p
       should be determined by X.
       Use myQRC inside of this function
       
#############################################
## FILL IN THE BODY OF THIS FUNCTION BELOW ##
#############################################
       
       */  
       int n = X.n_rows;
       int p = X.n_cols;
       
       mat O;
       O.ones(n,1);
       mat M = join_rows(O,X);
       mat A = join_rows(M,Y);
       
       mat R = myQRC(A)["R"];
       mat R1 = R(span(0,p),span(0,p));
       mat Y1 = R(span(0,p),(p+1));
       mat beta_ls = (R1.i() * Y1).t();
       
       // Function returns the 'p+1' by '1' matrix 
       // beta_ls of regression coefficient estimates
       return(beta_ls.t());
       
}  

/* ~~~~~~~~~~~~~~~~~~~~~~~~ 
Problem 3: PCA based on QR 
~~~~~~~~~~~~~~~~~~~~~~~~~~ */


// [[Rcpp::export()]]
List myEigen_QRC(const mat A, const int numIter = 1000){
       
       /*  
       
       Perform PCA on matrix A using your QR function, myQRC.
       Input:
       A: Square matrix
       numIter: Number of iterations
       
#############################################
## FILL IN THE BODY OF THIS FUNCTION BELOW ##
#############################################
       
       */  
       List output;
       
       mat B = A;
       int p = A.n_cols;
       mat V;
       V.randn(p,p);
       for (int i=0; i<=numIter; i++) {
              mat Q = myQRC(V)["Q"] ;
              V = B * Q;
       }
       mat Q = myQRC(V)["Q"] ;
       mat R = myQRC(V)["R"] ;
       vec D = R.diag();
       
       // Function should output a list with D and V
       // D is a vector of eigenvalues of A
       // V is the matrix of eigenvectors of A (in the 
       // same order as the eigenvalues in D.)
       output["D"] = D;
       output["V"] = Q;
       return(output);
       
}
