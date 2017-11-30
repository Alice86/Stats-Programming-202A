#' Ridge regression
#'
#' This function perform ridge regression of Y on X with QR method, return the coefficient vector.
#' @param X design matrix
#' @param Y response vector
#' @param lambda regularization parameter (lambda >= 0)
#' @examples
#' n <- 100
#' p <- 4
#' X <- matrix(rnorm(n * p), nrow = n)
#' beta <- rnorm(p)
#' Y <- X %*% beta+rnorm(n)
#' lambda=1
#' myRidge(X, Y, lambda)
#' @export
myRidge <- function(X, Y, lambda){
       n <- nrow(X)
       p <- ncol(X)
       Z <- cbind(rep(1, n), X, Y)
       D <- diag(rep(sqrt(lambda), p))
       D <- cbind(rep(0,p),D,rep(0,p))
       A <- rbind(Z,D)
       R <- myQR(A)$R
       beta_ridge <- solve(R[1:(p+1), 1:(p+1)]) %*% R[1:(p+1),p+2]
       return(beta_ridge)
}
