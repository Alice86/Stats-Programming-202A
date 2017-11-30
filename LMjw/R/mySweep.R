#' Sweep operation
#'
#' This function perform a SWEEP operation on A with the pivot element A[m,m]
#' @param A a square matrix
#' @param m the pivot element is A[m, m]
#' @export
mySweep <- function(A, m){
       n <- dim(A)[1]
       for  (k in 1:m) {
              for (j in 1:n) {
                     for (i in 1:n) {
                            if (i != k & j != k) {
                                   A[i,j] <- A[i,j]-A[i,k]*A[k,j]/A[k,k]
                            }
                     }}
              for (i in 1:n) {
                     if (i != k) {
                            A[i,k] <- A[i,k]/A[k,k]
                     }
              }
              for (j in 1:n) {
                     if (j!=k) {
                            A[k,j] <- A[k,j]/A[k,k]
                     }
              }
              A[k,k] <- - 1/A[k,k]
       }
       return(A)
}
