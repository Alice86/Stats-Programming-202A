#########################################################
## Stat 202A - Final Project
## Author: Jiayu Wu
## Date: 12/15/2017
## Description: This script implements a two layer neural network
#########################################################

#############################################################
## INSTRUCTIONS: Please fill in the missing lines of code
## only where specified. Do not change function names,
## function inputs or outputs. You can add examples at the
## end of the script (in the "Optional examples" section) to
## double-check your work, but MAKE SURE TO COMMENT OUT ALL
## OF YOUR EXAMPLES BEFORE SUBMITTING.
##
## Very important: Do not use the function "os.chdir" anywhere
## in your code. If you do, I will be unable to grade your
## work since Python will attempt to change my working directory
## to one that does not exist.
#############################################################
import numpy as np
import csv
import random
import math
import matplotlib.pyplot as plt

def prepare_data(valid_digits=np.array((6,5))):
    if len(valid_digits)!=2:
        raise Exception("Error: you must specify exactly 2 digits for classification!")

    csvfile=open('digits.csv','r')
    reader=csv.reader(csvfile)
    data=[]
    for line in reader:
        data.append(line)

    csvfile.close()
    digits=np.asarray(data,dtype='float')

    X=digits[(digits[:,64]==valid_digits[0]) | (digits[:,64]==valid_digits[1]),0:64]
    Y = digits[(digits[:, 64] == valid_digits[0]) | (digits[:, 64] == valid_digits[1]), 64:65]

    X=np.asarray(map(lambda k: X[k,:]/X[k,:].max(), range(0,len(X))))

    Y[Y==valid_digits[0]]=0
    Y[Y==valid_digits[1]]=1

    training_set=random.sample(range(360),270)

    testing_set=list(set(range(360)).difference(set(training_set)))

    X_train=X[training_set,:]
    Y_train=Y[training_set,]

    X_test=X[testing_set,:]
    Y_test=Y[testing_set,]

    return X_train,Y_train,X_test,Y_test


def accuracy(p,y):

    acc=np.mean((p>0.5)==(y==1))
    return acc

####################################################
## Two Layer Neural Network  ##
####################################################

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Train a two layer neural network to classify the digits data ##
## Use Relu as the activation function for the first layer. Use Sigmoid as the activation function for the second layer##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
def my_NN(X_train,Y_train,X_test,Y_test,num_hidden=20,num_iterations=1000,learning_rate=1e-1):

    n=X_train.shape[0]
    p=X_train.shape[1]+1
    ntest=X_test.shape[0]

    X_train1= np.concatenate((np.repeat(1,n,axis=0).reshape((n,1)),X_train),axis=1)
    X_test1 = np.concatenate((np.repeat(1, ntest, axis=0).reshape((ntest, 1)), X_test), axis=1)
    alpha=np.random.standard_normal((p,num_hidden))
    beta=np.random.standard_normal((num_hidden+1,1))
    acc_train=np.repeat(0.,num_iterations)
    acc_test=np.repeat(0.,num_iterations)

    #######################
    ## FILL IN CODE HERE ##
    #######################
    for it in range(0,num_iterations):
        h1 = np.maximum(np.dot(X_train1, alpha),0)
        h = np.concatenate((np.repeat(1,n,axis=0).reshape((n,1)),h1),axis=1)
        pr = 1/(1+np.exp(-np.dot(h,beta)))

        dbeta = np.mean((Y_train-pr).reshape(n,1)*h,axis=0)
        beta = beta + (learning_rate*dbeta).reshape(num_hidden+1,1)

        for k in range(0,num_hidden):
            da = (Y_train - pr)[:,0]*beta[k+1,0]*np.sign(h1[:,k])
            dalpha = np.mean(da.reshape(n,1)*X_train1,axis=0)
            alpha[:,k] = alpha[:,k] + learning_rate*dalpha
        
        acc_train[it] = accuracy(pr, Y_train)
        ht = np.maximum(np.dot(X_test1, alpha),0)
        htest = np.concatenate((np.repeat(1,ntest,axis=0).reshape((ntest,1)),ht),axis=1)
        prtest = 1/(1+np.exp(-np.dot(htest,beta)))
        acc_test[it] = accuracy(prtest, Y_test)    


    ## Function should output 4 things:
    ## 1. The learned parameters of the first layer of the neural network, alpha
    ## 2. The learned parameters of the second layer of the neural network, beta
    ## 3. The accuracy over the training set, acc_train (a "num_iterations" dimensional vector).
    ## 4. The accuracy over the testing set, acc_test (a "num_iterations" dimensional vector).
    return alpha,beta,acc_train,acc_test


############################################################################
## Test your functions and visualize the results here##
############################################################################
X_train, Y_train, X_test, Y_test = prepare_data()
alpha,beta,acc_train,acc_test=my_NN(X_train,Y_train,X_test,Y_test,num_hidden=50,num_iterations=1000,learning_rate=1e-2)

# Visualization
NN = my_NN(X_train,Y_train,X_test,Y_test,num_hidden=50,num_iterations=200,learning_rate=0.1)
for i in range(2,4):
     plt.figure(3)
     plt.plot(range(1,201), NN[i])
     plt.title('Accuracy Plot of Neural Network')# give plot a title
     plt.xlabel('Time of Iteration')# make axis labels
     plt.ylabel('Accuracy')
     plt.legend(('Traning', 'Testing'))

####################################################
## Optional examples (comment out your examples!) ##
####################################################
#def my_SVM(X_train, Y_train, X_test, Y_test, lamb=0.01, num_iterations=200, learning_rate=0.1):
#    n = X_train.shape[0]
#    p = X_train.shape[1] + 1
#    X_train1 = np.concatenate((np.repeat(1, n, axis=0).reshape((n, 1)), X_train), axis=1)
#    Y_train = 2 * Y_train - 1
#    beta = np.repeat(0., p, axis=0).reshape((p, 1))
#
#    ntest = X_test.shape[0]
#    X_test1 = np.concatenate((np.repeat(1, ntest, axis=0).reshape((ntest, 1)), X_test), axis=1)
#    Y_test = 2 * Y_test - 1
#
#    acc_train = np.repeat(0., num_iterations, axis=0)
#    acc_test = np.repeat(0., num_iterations, axis=0)
#
#    for it in range(0,num_iterations):
#        score = np.dot(X_train1, beta)
#        delta = score * Y_train < 1
#        dbeta = np.sum(delta * np.multiply(Y_train, X_train1),axis=0)/n
#        beta = beta + learning_rate * dbeta.reshape(p,1)
#        beta[1:(p-1),0] = beta[1:(p-1),0] - lamb * beta[1:(p-1),0]
#        acc_train[it] = np.mean(np.sign(np.dot(X_train1, beta)) == Y_train)
#        acc_test[it] = np.mean(np.sign(np.dot(X_test1, beta)) == Y_test)
#
#    return beta, acc_train, acc_test
#
#def my_Adaboost(X_train, Y_train, X_test, Y_test, num_iterations=200):
#
#    n = X_train.shape[0]
#    p = X_train.shape[1]
#    threshold = 0.8
#
#    X_train1 = 2 * (X_train > threshold) - 1
#    Y_train = 2 * Y_train - 1
#
#    X_test1 = 2 * (X_test > threshold) - 1
#    Y_test = 2 * Y_test - 1
#
#    beta = np.repeat(0., p).reshape((p, 1))
#    w = np.repeat(1. / n, n).reshape((n, 1))
#
#    weak_results = np.multiply(Y_train, X_train1) > 0
#
#    acc_train = np.repeat(0., num_iterations, axis=0)
#    acc_test = np.repeat(0., num_iterations, axis=0)
#
#    for it in range(0,num_iterations):
#        w = w/sum(w)
#        a = np.dot(np.repeat(1,n).reshape(1,n),w * weak_results)
#        e = 1-a
#        k = np.argmin(e)
#        db = np.log((1-e[0,k])/e[0,k])/2
#        beta[k,0] = beta[k,0]+db
#        w = (w[:,0] * np.exp(-Y_train[:,0]*X_train1[:,k]*db)).reshape(n,1)
#        acc_train[it] = np.mean(np.sign(np.dot(X_train1, beta)) == Y_train)
#        acc_test[it] = np.mean(np.sign(np.dot(X_test1, beta)) == Y_test)
#
#    return beta, acc_train, acc_test
#
#np.random.seed(27)
#X_train, Y_train, X_test, Y_test = prepare_data()
#NN = my_NN(X_train,Y_train,X_test,Y_test,num_hidden=50,num_iterations=200,learning_rate=0.1)
#svm = my_SVM(X_train, Y_train, X_test, Y_test, lamb=0.01, num_iterations=200, 
#learning_rate=0.1)
#ab = my_Adaboost(X_train, Y_train, X_test, Y_test, num_iterations=200)
#
#import matplotlib.pyplot as plt
#for i in range(1,3):
#     plt.figure(1)
#     plt.plot(range(1,201), svm[i])
#     plt.title('Accuracy Plot of SVM')# give plot a title
#     plt.xlabel('Time of Iteration')# make axis labels
#     plt.ylabel('Accuracy')
#     plt.legend(('Traning', 'Testing'))
#     plt.figure(2)
#     plt.plot(range(1,201), ab[i])
#     plt.title('Accuracy Plot of Adaboost')# give plot a title
#     plt.xlabel('Time of Iteration')# make axis labels
#     plt.ylabel('Accuracy')
#     plt.legend(('Traning', 'Testing'))
#for i in range(2,4):
#     plt.figure(3)
#     plt.plot(range(1,201), NN[i])
#     plt.title('Accuracy Plot of Neural Network')# give plot a title
#     plt.xlabel('Time of Iteration')# make axis labels
#     plt.ylabel('Accuracy')
#     plt.legend(('Traning', 'Testing'))
