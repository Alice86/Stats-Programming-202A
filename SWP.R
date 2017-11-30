# SWP
mySweep <- function(A, m) {
       n <- dim(A)[1]
       d <- 1
       for  (k in 1:m) {
              d<-d*A[k,k]
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
                            A[k,j] <- - A[k,j]/A[k,k]
                     }      
              } 
              A[k,k] <- 1/A[k,k]
       }
       return(list(A,d))
}

A<-matrix(c(),3,3)
solve(A)
mySweep(A,3)

A <- t(Z) %*% Z
A <- mySWPC(A,p+1)
beta_hat <- A[1:(p+1),p+2]
sigm.sq <- A[p+2,p+2]/(n-p-1)

X= matrix(rnorm(n*p),nrow=n)
beta=matrix(1:p,nrow=p)
Y=X%*%beta+rnorm(n)

## Define parameters
n <- nrow(X)
p <- ncol(X)
Z = cbind(rep(1,n),X,Y)
A=t(Z)%*%Z

# Rccp