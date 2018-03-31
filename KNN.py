# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 19:51:30 2018

@author: 03
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
#print(X)
X=np.array(X)
X=X.astype(float)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
X_train=np.array(X_train)
y_train=np.array(y_train)
X_test=np.array(X_test)
y_test=np.array(y_test)
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train,y_train)
KNeighborsClassifier(algorithm='auto',leaf_size=30,metric='minkowski',metric_params=None,n_jobs=1,n_neighbors=5,p=2,weights='uniform')
a=neigh.predict(X_test)
s=0
for i in range(0,len(y_test)):
    if a[i]==y_test[i]:
        s=s+1
print(s/len(y_test))
#X = [[0], [1], [2], [3]]
#y = [0, 0, 1, 1]
#from sklearn.neighbors import KNeighborsClassifier
#neigh = KNeighborsClassifier(n_neighbors=3)
#neigh.fit(X, y) 
#KNeighborsClassifier()
#print(neigh.predict([[1.1]]))