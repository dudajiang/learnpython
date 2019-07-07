'''

模拟生成20000行数据，y=2X+3
用tensorflow的线性回归进行模拟，并将生成的模型存储下来，并对一个随机的数据集进行预估结果

1、用numpy模拟生成随机数据，
1）生成一个pd模型
2）将pd模型存储到csv中
3）可以将pd用图形方式呈现出来
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_X = np.random.randint(0,500,size=2000)
train_Y = 2 * train_X * train_X + np.random.randn(2000)*100

df1 = pd.DataFrame(data=train_X,columns=['trainx'])
df2 = pd.DataFrame(data=train_Y,columns=['trainy'])
print(df1)

df = pd.concat([df1,df2],axis=1)
print(df)

df.to_csv('0301.csv')

# plt.plot(train_X,train_Y,'ro',label='data')
# plt.legend()
# plt.show()
