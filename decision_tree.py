# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:45:09 2018

@author: 姜兴琪
"""

import numpy as np
from sklearn.cross_validation import train_test_split
import csv
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

print (len(X_train),len(y_train))
print (len(X_test),len(y_test))

from sklearn.tree import DecisionTreeClassifier
# Train
clf = DecisionTreeClassifier().fit(X_train, y_train)
a=clf.predict(X_test)
s=0
for i in range(0,len(y_test)):
    if (a[i]-y_test[i])==0:
        s=s+1
print (s/len(y_test))