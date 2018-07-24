# -*- coding: utf-8 -*-
"""

 Stat 202A - Homework 1
 Author: Jiayu WU
 Date : 10122017
 Description: This script implements linear regression 
 using Gauss-Jordan elimination in both plain and
 vectorized forms

 INSTRUCTIONS: Please fill in the missing lines of code
 only where specified. Do not change function names, 
 function inputs or outputs. You can add examples at the
 end of the script (in the "Optional examples" section) to 
 double-check your work, but MAKE SURE TO COMMENT OUT ALL 
 OF YOUR EXAMPLES BEFORE SUBMITTING.

 Do not use any of Python's built in functions for matrix 
 inversion or for linear modeling (except for debugging or 
 in the optional examples section).
 
"""

import numpy as np

###############################################
## Function 1: Plain version of Gauss Jordan ##
###############################################


def myGaussJordan(A, m):
  
  """
  Perform Gauss Jordan elimination on A.
  
  A: a square matrix.
  m: the pivot element is A[m, m].
  Returns a matrix with the identity matrix 
  on the left and the inverse of A on the right. 

  FILL IN THE BODY OF THIS FUNCTION BELOW 
  """
  n = A.shape[0]
  B = np.hstack((A, np.identity(n)))
  for k in range(m):
    a = B[k,k]
    for j in range(n*2):
        B[k,j] = B[k,j]/a
    for i in range(n):
        if i !=k:
            b = B[i,k]
            for j in range(n*2):
                B[i,j]=B[i,j]-B[k,j]*b
        
  ## Function returns the np.array B
  return B
  


####################################################
## Function 2: Vectorized version of Gauss Jordan ##
####################################################

def myGaussJordanVec(A, m):
  
  """
  Perform Gauss Jordan elimination on A.
  
  A: a square matrix.
  m: the pivot element is A[m, m].
  Returns a matrix with the identity matrix 
  on the left and the inverse of A on the right.
  
  FILL IN THE BODY OF THIS FUNCTION BELOW
  """
  n = A.shape[0]
  C = np.hstack((A, np.identity(n)))
  for k in range(m):
     C[k,:] = C[k,:]/C[k,k]
     for i in range(n):
        if i !=k:
            C[i,:]=C[i,:]-C[k,:]*C[i,k]
  
  ## Function returns the np.array B
  return B
  

######################################################
## Function 3: Linear regression using Gauss Jordan ##
######################################################

def myLinearRegression(X, Y):
  
  """
  Find the regression coefficient estimates beta_hat
  corresponding to the model Y = X * beta + epsilon
  Your code must use one of the 2 Gauss Jordan 
  functions you wrote above (either one is fine).
  Note: we do not know what beta is. We are only 
  given a matrix X and a vector Y and we must come 
  up with an estimate beta_hat.
  
  X: an 'n row' by 'p column' matrix (np.array) of input variables.
  Y: an n-dimensional vector (np.array) of responses

  FILL IN THE BODY OF THIS FUNCTION BELOW
  """
  
  ## Let me start things off for you...
  n = X.shape[0]
  p = X.shape[1]                         
  Z = np.hstack((np.repeat(1,n).reshape(n,1),X,Y))
  A= np.dot(Z.T,Z)
  S= myGaussJordanVec(A,p+1)
  beta_hat = S[0:p+1,p+1]
  
  ## Function returns the (p+1)-dimensional vector (np.array) 
  ## beta_hat of regression coefficient estimates
  return beta_hat
  

########################################################
## Optional examples (comment out before submitting!) ##
########################################################

## def testing_Linear_Regression():
  
  ## This function is not graded; you can use it to 
  ## test out the 'myLinearRegression' function 

  ## You can set up a similar test function as was 
  ## provided to you in the R file.
  
n=100
p=3
np.random.seed(7)
X = np.random.normal(0,1,n*p).reshape(n,p)
beta=np.arange(1, p+1, 1).reshape(p,1)
Y =np.dot(X,beta)+np.random.normal(0,1,n).reshape(n,1)
myCoef = myLinearRegression(X, Y)

import matplotlib.pyplot as plt
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X,Y)
PCoef = np.hstack((regr.intercept_.reshape(1,1),regr.coef_))
diff = sum((PCoef - myCoef)^2)
  