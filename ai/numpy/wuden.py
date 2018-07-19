#!/usr/bin/env python
# coding:utf8
import numpy as np
import numpy.random as npr
import numpy.linalg as nla
import pandas as pd

data = [[7,5,2],
[3,0,9],
[0,6,8]]

# 将list转化成numpy中的ndarray
nd = np.array(data)
print(nd)

div = nla.inv(nd)

print(div)

a = nd.dot(div)
b = div.dot(nd)

print(a)
print(b)


