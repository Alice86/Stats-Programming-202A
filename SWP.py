#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:01:04 2017

@author: alice
"""

import numpy as np  

def mySweep(A, m):
    
    B = np.copy(A)   
    n = B.shape[0]
    
    for k in range(m):
        for i in range(n):
            for j in range(n):
                if i<>k and j<>k:
                    B[i,j] = B[i,j]-B[i,k]*B[k,j]/B[k,k];                
        for i in range(n):
            if i<>k:
                B[i,k]=B[i,k]/B[k,k];
        for j in range(n):
            if j<>k:
                B[k,j]= B[k,j]/B[k,k];
        B[k,k] = - 1/B[k,k];
    
    return(B)

# debug
n=100
p=3
np.random.seed(7)
X = np.random.normal(0,1,n*p).reshape(n,p)
beta=np.arange(1, p+1, 1).reshape(p,1)
Y =np.dot(X,beta)+np.random.normal(0,1,n).reshape(n,1)

Z = np.hstack((np.repeat(1,n).reshape(n,1),X,Y))
A = np.dot(Z.T,Z)

np.linalg.inv(A)
mySweep(A, 5)




D = myGI(A,1)
def myGI(A,m):
    n = A.shape[0]
    B = np.hstack([A, np.identity(n)])
    for k in range(m):
        B[k,:] = B[k,:]/B[k,k]
        # a = B[k,k]
        # for j in range(n*2):
        #    B[k,j] = B[k,j]/a
        for i in range(n):
            if i !=k:
                B[i,:]=B[i,:]-B[i,:]*B[i,k]
                # b = B[i,k]
                # for j in range(n*2):
                #     B[i,j]=B[i,j]-B[k,j]*b
    return B

