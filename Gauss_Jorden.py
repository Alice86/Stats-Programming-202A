#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:03:30 2017

@author: alice
"""

# import package
import numpy as np

# function for appling Gauss-Jordan for 1 : m on A
def myGI(A,m):
    n = A.shape[0]
    B = np.hstack(A, np.identity(n))
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
        print B