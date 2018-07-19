#!/usr/bin/env python
# coding:utf8

import numpy as np
import matplotlib.pyplot as plt
# from sklearn import svm, datasets

# iris = datasets.load_iris()
# # Take the first two features. We could avoid this by using a two-dim dataset
# X = iris.data[:, :2]
# y = iris.target

x=np.linspace(-np.pi,np.pi,500,endpoint=True)  
print(x)
C=np.cos(x)
S=np.sin(x)  
plt.plot(x,C)  
plt.plot(x,S) 

plt.show()