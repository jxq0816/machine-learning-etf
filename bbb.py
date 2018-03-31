# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:45:09 2018

@author: 38991
"""

import numpy as np  
from sklearn.cross_validation import train_test_split
import csv  
#from itertools import islice  
with open(r'etf_data/c510050.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')  
    hearder=next(readCSV)
    X = []  
    y = []  
    for row in readCSV:  
        X.append(np.array(row[0:6]))
        y.append(int(row[-1])) 
X=np.array(X)
X=X.astype(float)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3) 
X_train=np.array(X_train)
y_train=np.array(y_train)
X_test=np.array(X_test)
y_test=np.array(y_test)

#print (len(X_test),len(y_test))
from sklearn.naive_bayes import GaussianNB  
clf = GaussianNB().fit(X_train, y_train)  
a=clf.predict(X_test)
s=0
for i in range(0,len(y_test)):
    if (a[i]-y_test[i])!=0:
        s=s+1
print (s/len(y_test))
''''' 
partial_fit说明：增量的训练一批样本 
这种方法被称为连续几次在不同的数据集，从而实现核心和在线学习，这是特别有用的，当数据集很大的时候，不适合在内存中运算 
该方法具有一定的性能和数值稳定性的开销，因此最好是作用在尽可能大的数据块（只要符合内存的预算开销） 
'''  
#clf_pf = GaussianNB().partial_fit(X, Y, np.unique(Y))  
#print (clf_pf.predict([[-0.8,-1]]))  
#import numpy as np  
#X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])  
#Y = np.array([1, 1, 1, 2, 2, 2])  
#from sklearn.naive_bayes import GaussianNB  
#clf = GaussianNB().fit(X, Y)  
#print (clf.predict([[-0.8,-1]])  )
#  
#''''' 
#partial_fit说明：增量的训练一批样本 
#这种方法被称为连续几次在不同的数据集，从而实现核心和在线学习，这是特别有用的，当数据集很大的时候，不适合在内存中运算 
#该方法具有一定的性能和数值稳定性的开销，因此最好是作用在尽可能大的数据块（只要符合内存的预算开销） 
#'''  
#clf_pf = GaussianNB().partial_fit(X, Y, np.unique(Y))  
#print (clf_pf.predict([[-0.8,-1]]) ) 