# function for appling Gauss-Jordan for 1 : m on A
myGI <- function (A,m) {
       n<-dim(A)[1]
       B<-cbind(A,diag(rep(1,n)))
       for (k in 1:m) {
              B[k,] <- B[k,]/B[k,k] #row operation
              # a <- B[k,k]
              # for (j in 1:(n*2)){
              #       B[k,j] <- B[k,j]/a
              #} 
              for (i in 1:n) {
                     if (i != k) {
                            b <- B[i,k]
                            B[i,] <- B[i,]-b*B[k,]
                            #for (i in 1:(n*2)) {
                            #       B[i,j] <- B[i,j]-b*B[k,j]
                            #} 
                     }
              }
                     
       }
       return(B)
}

# Simulation
set.seed(7)
n=100
p=5
X= matrix(rnorm(n*p),nrow=n)
beta=matrix(1:p,nrow=p)
Y=X%*%beta+rnorm(n)
lm1<-lm(Y~X)
summary(lm1)

# Test with simulation
Z = cbind(rep(1,n),X,Y)
A=t(Z)%*%Z
S=myGI(A,p+1)
e_beta = S[1:(p+1),p+2] # lm1$coefficients
RSS = S[p+2,p+2] # sum(lm1$residuals^2)
vcov(lm.object) = S[1:(p+1),(p+3):(2*p+3)]
