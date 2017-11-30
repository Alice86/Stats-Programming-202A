#' Logistic regression
#'
#' This function perform logistic regression of Y on X with IRLS method, return the IRLS solution vector.
#' @param X design matrix
#' @param Y response vector
#' @examples
#' n <- 100
#' p <- 4
#' X <- matrix(rnorm(n * p), nrow = n)
#' beta <- rnorm(p)
#' expit <- function(x){
#'       1 / (1 + exp(-x))
#' }
#' Y <- 1 * (runif(n) < expit(X %*% beta))
#' myLogistic(X, Y)
#' @export
myLogistic <- function(X, Y){
       n <- nrow(X)
       m <- ncol(X)
       expit <- function(x){
              1 / (1 + exp(-x))
       }
       beta <- matrix(rep(0,m),nrow = m)
       epsilon <- 10^(-6)
       err <- 1

       while (err >= epsilon) {
              eta <- X %*% beta
              p <- expit(eta)
              w <- p*(1-p)
              Y_hat <- eta + (Y-p)/w
              wm <- matrix(rep(sqrt(w),each=m),byrow=T,ncol = m) 

              X_ls <- wm * X
              Y_ls <- sqrt(w) * Y_hat
              beta_n <- t(myLM(X_ls, Y_ls, intercept=FALSE)$beta_ls)
              err <- sum(abs(beta_n-beta))
              beta <- beta_n
       } 
       p <- expit(X %*% beta)
       w <- p*(1-p)
       X_ls <-  matrix(rep(sqrt(w),each=m),byrow=T,ncol = m) * X
       se <- sqrt(diag(solve(t(X_ls)%*%X_ls)))
       #se <- myLM(X_ls, Y_ls, intercept=FALSE)$se
       output <- list(beta=beta, se=se)
       return(output)
}
