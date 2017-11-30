#' Lasso regression
#'
#' This function finds lasso solution path for various values of regularization parameter of Y regressed on X, return a matrix with each column corresponding to a regularization parameters.
#' @param X design matrix
#' @param Y response vector
#' @param lambda_all vector of regularization parameters
#' @examples
#' n <- 50
#' p <- 25
#' X <- matrix(rnorm(n * p), nrow = n)
#' beta <- c(rep(0,20),rep(1,5))
#' Y <- X %*% beta+rnorm(n)
#' lambda_all <- (100:1)/10
#' lasso <- myLasso(X,Y,lambda_all)
#' beta_sum <- t(matrix(rep(1, (p+1)), nrow = 1)%*%abs(beta_all))
#' matplot(beta_sum, t(beta_all), type = 'l', lty = 1,xlab="|beta|",ylab="beta")
#' text(max(beta_sum),beta_all[,length(lambda_all)],0:p,cex=1,col=1:p)
#' @export
myLasso <- function(X, Y, lambda_all){
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
       return(beta_all)
}
