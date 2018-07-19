#!/usr/bin/env python
# coding:utf8

from sklearn import svm
import numpy as np

X = [[0,0],[1,1],[1,2],[2,2],[2,0],[3,2]]
y = [0,2,3,4,2,5]
clf = svm.SVC()
print clf
clf.fit(X,y)
result =  clf.predict([[2,3]])
# result1 = clf.predict_proba([[2,2]])
print result
# print result1