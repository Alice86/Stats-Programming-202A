#' Linear regression
#'
#' This function perform linear regression of Y on X powered by QR decomposition, return a list of the least squares solution vector.
#' @param X design matrix
#' @param Y response vector
#' @param intercept whether the model contains an intercept, default to TRUE
#' @examples
#' n <- 100
#' p <- 4
#' X <- matrix(rnorm(n * p), nrow = n)
#' beta <- rnorm(p)
#' Y <- X %*% beta+rnorm(n)
#' myLM(X, Y, intercept=FALSE)
#' @export
myLM <- function(X, Y, intercept=TRUE){
       n <- nrow(X)
       p <- ncol(X)
       if (intercept==TRUE) {
              A <- cbind(rep(1,n),X,Y)
              p <- p+1
       } else {A <- cbind(X,Y)}
       R <- myQR(A)$R
       R1 = R[1:p,1:p]
       Y1 = R[1:p,p+1]
       beta_ls <- t(solve(R1)%*%Y1)
       sigma.sq <- sum(R[(p+1):n,p+1]^2)/(n-p)
       se <- sqrt(rep(sigma.sq,p)*diag(solve(t(A[,1:p])%*%A[,1:p])))

       output <- list(beta_ls=beta_ls, se=se)
       return(output)

}
