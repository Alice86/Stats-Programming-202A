#' QR decomposition
#'
#' This function perform QR decomposition on the matrix A, return a list of orthogonal matrix Q and upper triangular matrix R
#' @param A input matrix
#' @examples
#' A <- matrix(rnorm(25),nrow=5);
#' myQR(A)
#' @export
myQR <- function(A){
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
       return(list("Q" = t(Q), "R" = R))

}
