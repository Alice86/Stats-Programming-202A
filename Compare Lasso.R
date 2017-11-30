set.seed(10086)
n <- 50
p <- 200
X <- matrix(rnorm(n * p), nrow = n)
beta <- c(1:5,rep(0,195))
Y <- 1+X %*% beta+rnorm(n)

myLasso_w <- function(X, Y, lambda_all){
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

myLasso_n <- function(X, Y, lambda_all){
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
       for(l in 1:L) {
              lambda <- lambda_all[l]
              beta <- beta_all[,l]
              R <- Y
              for(t in 1:10) {
                     for(k in 1:p) {
                            R <- R + X[,k]*beta[k]
                            b <- sum(R*X[,k])/SS[k]
                            b <- sign(b)*max(0,abs(b)-lambda/S[k])
                            R <- R - X[,k]*b
                            beta[k] <- b
                     }
              }
              beta_all[,l] <- beta
       }
       return(beta_all)
}

lambda_all <- (100:1)*10
beta1 <- myLasso_w(X,Y,lambda_all)
beta2 <- myLasso_n(X,Y,lambda_all)
beta1 == beta2

beta_sum <- t(matrix(rep(1, (p+1)), nrow = 1)%*%abs(beta1))
matplot(beta_sum, t(beta1), type = 'l',
        lty = 1,xlab="|beta|", ylab="beta")

beta_sum <- t(matrix(rep(1, (p+1)), nrow = 1)%*%abs(beta2))
matplot(beta_sum, t(beta2), type = 'l',
         lty = 1,xlab="|beta|",ylab="beta")
