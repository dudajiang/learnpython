#!/usr/bin/env python
# coding:utf8
import numpy as np
import numpy.random as npr
import pandas as pd

data = [[7,5,2],
[3,0,9],
[0,6,8],
[1,5,5],
[6,1,7]]

# 将list转化成numpy中的ndarray
nd = np.array(data)
print(nd)

# # 将list转化成pandas中的series
# ser = pd.Series(data,index=['one','two','three','four','five'])

# # 将list转化成pandas中的dataframe
df = pd.DataFrame(data=nd)

# # 将series转化成numpy中的ndarray
# foo = ser.as_matrix()

# 将dataframe转化成numpy中的ndarray
foo1 = df.as_matrix([0,1])
foo2 = df.values
foo3 = np.array(df)



# print(data)
# print(ser)
print(df)
print(foo3)
print(foo1)
print(foo2)







