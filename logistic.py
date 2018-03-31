# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:50:44 2018

@author: wangzhao
"""
import pandas as pd
import numpy as np
from numpy import *

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def stocGradAscent1(dataMatrix,classLabels,numIter=150):
    m,n = shape(dataMatrix)
    #print(shape(dataMatrix))
    weights = ones(n)
    #print(shape(weights))
    for j in range(numIter):
        for i in range(m):
            dataIndex = list(range(m))
            #print(dataIndex)
            alpha = 4/(1.0+j+i)+0.01
            randIndex = int(random.uniform(0,len(dataIndex)))
            #print(randIndex)
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex]-h
            #print(error)
            #weights=np.array()
            #print(shape(dataMatrix[randIndex]))
            #we=alpha*error*np.float64(dataMatrix[randIndex])
            #weights=weights+we
            weights = weights+alpha*error*np.float64(dataMatrix[randIndex])
            #print(shape(dataMatrix[randIndex]))
            del(dataIndex[randIndex])
    
    #m1,n2 =shape(weights)
    #print('----')
    #print(shape(weights))
    return weights

def classifyVector(inX,weights):
    #print(inX)
    #print(weights)
    #print(np.shape(inX))
    #print(np.shape(weights))
    prob = sigmoid(sum(np.float64(inX)*weights))
    if prob>0.5:
        return 1.0
    else:
        return 0.0
    
def colicTest():
    frTrain = open('eft_data/logistic_train.txt')
    frTest = open('eft_data/logistic_test.txt')
    trainingSet = []
    trainingLabels=[]
    
    for line in frTrain.readlines():
        #print(line)
        currLine = line.strip().split(' ')
        lineArr = []
        for i in range(6):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[6]))

    
    trainWeights = stocGradAscent1(trainingSet,trainingLabels,450)
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec +=1.0
        currLine = line.strip().split(' ')
        lineArr =[]
        for i in range(6):
            #lineArr.append(float(currLine[i]))
            lineArr.append(float(currLine[i]))
        #print('-------')
        #print(currLine[6])
        #print(classifyVector(array(lineArr),trainWeights))
        #print('-------')
        currLine[6]=float(currLine[6])
        if int(classifyVector(array(lineArr),trainWeights))!=int(currLine[6]):
            errorCount+=1
    #print(errorCount)
    #print(numTestVec)
    errorRate = (float(errorCount)/numTestVec)
    #print("the error rate of this test is :%f"%errorRate)
    return errorRate

def multiTest():
    numTests = 20
    errorSum = 0.0
    for k in range(numTests):
        errorSum +=colicTest()
    print("after %d iterations the average error rate is :%f"%(numTests,errorSum/float(numTests)))
    
