x#############################################################
## Stat 202A - Homework 7
## Author: Jiayu Wu
## Date: 11/28/2017
## Description: This script implements the lasso
#############################################################

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

#####################################
## Function 1: Lasso solution path ##
#####################################

myLasso <- function(X, Y, lambda_all){

       # Find the lasso solution path for various values of
       # the regularization parameter lambda.
       #
       # X: n x p matrix of explanatory variables.
       # Y: n dimensional response vector
       # lambda_all: Vector of regularization parameters. Make sure
       # to sort lambda_all in decreasing order for efficiency.
       #
       # Returns a matrix containing the lasso solution vector
       # beta for each regularization parameter.

       #######################
       ## FILL IN CODE HERE ##
       #######################
       n <- nrow(X)
       X <- cbind(rep(1,n),X)
       p <- ncol(X)
       L <- length(lambda_all)
       SS <- rep(0,p)
       for(j in 1:p) {
              SS[j] <- sum(X[ ,j]^2)
       }
       S <- SS
       S[1] <- Inf
       beta_all <- matrix(rep(0,p*L), nrow=p)
       beta <-  matrix(rep(0,p), nrow=p)
       R <- Y
       for(l in 1:L) {
              lambda <- lambda_all[l]
              for(t in 1:10) {
                     for(k in 1:p) {
                            db <- sum(R*X[,k])/SS[k]
                            b <- beta[k] + db
                            b <- sign(b)*max(0, abs(b)-lambda/S[k])
                            db <- b-beta[k]
                            R <- R - X[ ,k]*db
                            beta[k] <- b
                     }
              }
              beta_all[,l] <- beta
       }

       ## Function should output the matrix beta_all, the
       ## solution to the lasso regression problem for all
       ## the regularization parameters.
       ## beta_all is (p+1) x length(lambda_all)
       return(beta_all)

}

# p <- ncol(X)
# beta_sum <- t(matrix(rep(1, (p+1)), nrow = 1)%*%abs(beta_all))
# matplot(beta_sum, t(beta_all), type = 'l', main="Lasso Solution Path",lty = 1,xlab="|beta|",ylab="beta")
# text(max(beta_sum),beta_all[,length(lambda_all)],0:p,cex=1,col=1:p)
