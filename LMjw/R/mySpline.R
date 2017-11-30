#' Spline regression
#'
#' This function perform one-dimensional spline regression of Y on x with ridge regularization, return a list containing the spline regression coefficient vector and the predicted Y values.
#' @param x n x 1 vector or matrix of explanatory variables
#' @param Y n x 1 response vector
#' @param lambda regularization parameter (lambda >= 0)
#' @param p number of knots to make to the x-axis
#' @examples
#' n = 20
#' p = 100
#' sigma = 0.1
#' lambda = 1
#' x = runif(n)
#' x = sort(x)
#' x = matrix(x, nrow=n)
#' Y = x^2 + rnorm(n)*sigma
#' @export
mySpline <- function(x, Y, lambda, p = 100){
       n <- nrow(x)
       od <- order(x)
       X <- matrix(x[od,],nrow = n)
       x <- x[od,]
       Y <- matrix(Y[od,],nrow = n)
       interval <- (tail(x,1)-head(x,1))/p
       for (i in 1:(p-1)) {
              k <- head(x,1) + (i-1)*interval
              X <- cbind(X, matrix((x>k)*(x-k),nrow = n))
       }
       beta_spline <- myRidge(X, Y, lambda)
       Yhat <- cbind(rep(1, n), X)%*%beta_spline
       output <- list(beta_spline = beta_spline, predicted_y = Yhat)
       return(output)
}
