#########################################################
## Stat 202A - Homework 4
## Author: Jiayu Wu
## Date : 1031201789056
## Description: This script implements logistic regression
## using iterated reweighted least squares using the code 
## we have written for linear regression based on QR 
## decomposition
#########################################################

#############################################################
## INSTRUCTIONS: Please fill in the missing lines of code
## only where specified. Do not change function names, 
## function inputs or outputs. You can add examples at the
## end of the script (in the "Optional examples" section) to 
## double-check your work, but MAKE SURE TO COMMENT OUT ALL 
## OF YOUR EXAMPLES BEFORE SUBMITTING.
##
## Very important: Do not use the function "setwd" anywhere
## in your code. If you do, I will be unable to grade your 
## work since R will attempt to change my working directory
## to one that does not exist.
#############################################################


################ Optional ################ 
## If you are using functions from Rcpp, 
## uncomment and adjust the following two 
## lines accordingly. Make sure that your 
## cpp file is in the current working
## directory, so you do not have to specify
## any directories in sourceCpp(). For 
## example, do not write
## sourceCpp('John_Doe/Homework/Stats202A/QR.cpp')
## since I will not be able to run this.

# library(Rcpp)
# sourceCpp("QR.cpp")

##################################
## Function 1: QR decomposition ##
##################################

myQR <- function(A){
       
       ## Perform QR decomposition on the matrix A
       ## Input: 
       ## A, an n x m matrix
       
       ########################
       ## FILL IN CODE BELOW ##
       ########################  
       n <- nrow(A)
       m <- ncol(A)
       R <- A
       Q <- diag(n)
       for (i in 1:(m-1)) {
              X <- matrix(rep(0,n),nrow = n)
              X[i:n] <- R[i:n,i]
              V <- X
              V[i] <- X[i]+norm(X,"F")*sign(X[i])
              U <- V/norm(V,"F")
              R <- R-2*(U%*%t(U)%*%R)
              Q <- Q-2*U%*%t(U)%*%Q
       }
       
       ## Function should output a list with Q.transpose and R
       ## Q is an orthogonal n x n matrix
       ## R is an upper triangular n x m matrix
       ## Q and R satisfy the equation: A = Q %*% R
       return(list("Q" = t(Q), "R" = R))
       
}

###############################################
## Function 2: Linear regression based on QR ##
###############################################

myLM <- function(X, Y){
       
       ## Perform the linear regression of Y on X
       ## Input: 
       ## X is an n x p matrix of explanatory variables
       ## Y is an n dimensional vector of responses
       ## Use myQR (or myQRC) inside of this function
       
       ########################
       ## FILL IN CODE BELOW ##
       ########################  
       n <- nrow(X)
       p <- ncol(X)
       A <- cbind(X,Y)
       
       R <- myQR(A)$R
       R1 = R[1:p,1:p]
       Y1 = R[1:p,p+1]
       beta_ls <- solve(R1)%*%Y1
       
       ## Function returns the least squares solution vector
       return(beta_ls)
       
}

######################################
## Function 3: Logistic regression  ##
######################################

## Expit/sigmoid function
expit <- function(x){
       1 / (1 + exp(-x))
}

myLogistic <- function(X, Y){
       
       ## Perform the logistic regression of Y on X
       ## Input: 
       ## X is an n x p matrix of explanatory variables
       ## Y is an n dimensional vector of binary responses
       ## Use myLM (or myLMC) inside of this function
       
       ########################
       ## FILL IN CODE BELOW ##
       ########################
       n <- nrow(X)
       m <- ncol(X)
       
       beta <- matrix(rep(0,m),nrow = m)
       epsilon <- 10^(-6)
       err <- 1
       
       while (err >= epsilon) {
              eta <- X %*% beta
              p <- expit(eta)
              w <- p*(1-p)
              Y_hat <- eta + (Y-p)/w
              
              X_ls <- matrix(rep(sqrt(w),each=m),byrow=T,ncol = m) * X
              Y_ls <- sqrt(w) * Y_hat
              beta_n <- myLM(X_ls, Y_ls)
              err <- sum(abs(beta_n-beta))
              beta <- beta_n
       }
       
       ## Function returns the logistic regression solution vector
       beta  
       
}


## Optional testing (comment out!)
# set.seed(1) 
# n <- 100
# p <- 4
 
# X    <- matrix(rnorm(n * p), nrow = n)
# beta <- rnorm(p)
# Y    <- 1 * (runif(n) < expit(X %*% beta))
# 
# logistic_beta <- myLogistic(X, Y)
# logistic_beta    
