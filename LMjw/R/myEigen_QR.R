#' PCA
#'
#' This function perform PCA on matrix A based on eigen decomposition with power method, return a list of the eigen value vector D and the matrix of eigen vectors V.
#' @param A variance covariance matrix
#' @param numIter number of iteration, default to 1000
#' @examples
#' M <- matrix(rnorm(25),nrow=5);
#' A <- t(M) %*% M
#' myEigen_QR(A)
#' @export
myEigen_QR <- function(A, numIter = 1000){
       r <- dim(A)[1]
       v <- matrix(rnorm(r^2),nrow=r)
       for (i in 1:numIter) {
              QR <- myQR(v)
              Q = QR$Q
              R = QR$R
              v = A %*% Q
       }
       return(list("D" = diag(R), "V" = Q))

}
