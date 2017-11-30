myAdaboost <- function(X_train,Y_train,X_test,Y_test,T=3000) {
       n
       p
       for (t in 1:T) {
              w <- w/sum(w)
              a <- matrix(rep(1,n),nrow=1) %*% (matrix(w*Y_train,n,p)*X_train)
              e <- (1-a)/2
              k <- which.min(e)
              db <- log(1-e[k]/e[k])/2
              beta[k]<- beta[k]+db
              w<-w*exp(-y_train*X_train*db)
       }
}

# new members with strength current member don't have

T = 3000
epsilon = .0001
beta = matrix(rep(0, p), nrow = p)
db = matrix(rep(0, p), nrow = p)
beta_all = matrix(rep(0, p*T), nrow = p)
R=Y
for (t in 1:T)
{
}
for (j in 1:p)
       db[j] = sum(R*X[, j])
j = which.max(abs(db))
beta[j] = beta[j]+db[j]*epsilon
R = R - X[, j]*db[j]*epsilon
beta_all[, t] = beta
matplot(t(matrix(rep(1, p), nrow = 1)%*%abs(beta_all)), t(beta_all), type = ’l’)
