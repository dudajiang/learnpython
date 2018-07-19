import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.externals import joblib
import sklearn.metrics  as metrics
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv('polyline.csv',header=0))
# print(df)
XX = np.array(df)

# X存放XX中的第1到第5列，共5列
# y存放XX中的第6列，也就是通过X中
X = XX[:, 1:6]
y = XX[:, 6]

begin = 0
end = 1900

# 用来进行预测的数据10行
Xzhou = XX[begin:end,0]
Xpre = X[begin:end]
yreal = y[begin:end]

# #############################################################################
svrm = joblib.load("train_model.m")
y_rbf= svrm.predict(Xpre)

# #############################################################################
# Look at the results 用图展示结果
# lw = 2
# plt.scatter(Xzhou, yreal, color='darkorange', label='data')
# plt.plot(Xzhou, y_rbf, color='navy', lw=lw, label='RBF model')
# plt.xlabel('data')
# plt.ylabel('target')
# plt.title('Support Vector Regression')
# plt.legend()
# plt.show()

# #############################################################################
# Look at the results 用评估值对模型进行评估

a = metrics.explained_variance_score(yreal, y_rbf) 
b = metrics.mean_absolute_error(yreal, y_rbf)
c = metrics.mean_squared_error(yreal, y_rbf)
d = metrics.median_absolute_error(yreal, y_rbf)
e = metrics.r2_score(yreal, y_rbf)

print(a,b,c,d,e)