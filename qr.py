#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:06:13 2017

@author: alice
"""

import numpy as np 
from scipy import linalg

def qr(A):
    n,m=A.shape
    R=A.copy()
    Q=np.eye(n)
    for k in range(m-1):
        X = np.zeros((n,1))
        X[k:]=R[k:,k]
        V = X
        V[k]=X[k]+np.sign(X[k])*np.linalg.norm(X)
        S=np.linalg.norm(V)
        U=V/S
        R -= 2*np.dot(U,np.dot(U.T,R))
        Q -= 2*np.dot(U,np.dot(U.T,Q))
    Q=Q.T
    
    return Q,R

n=100
p=3

n = 100
p = 3
np.random.seed(7)
X = np.random.normal(0,1,n*p).reshape(n,p)
beta = np.arange(1, p+1, 1).reshape(p,1)
Y = np.dot(X,beta)+np.random.normal(0,1,n).reshape(n,1)

Z = np.hstack((np.repeat(1,n).reshape(n,1),X,Y))
Q,R = qr(Z)
R1 = R[:p+1,:p+1]
Y1 = R[:p+1,p+1]
beta = np.linalg.solve(R1,Y1)
print beta

def eigen_qr(A):
    T =  1000
    A_copy = A.copy
    r,c = A_copy.shape
    v = np.random.random_sample((r,r))
    for i in range(T):
        Q,R = qr(v)
        v =np.dot(A_copy,Q)
    
    return R.diagonal(),Q
        
        
        
        
        
        
        
        
        
        
        