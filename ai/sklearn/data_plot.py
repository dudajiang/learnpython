import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.externals import joblib
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv('polyline.csv',header=0))
# print(df)
XX = np.array(df)

# X存放XX中的第1到第5列，共5列
# y存放XX中的第6列，也就是通过X中
X = XX[:, 1:6]
y = XX[:, 6]

# 用来进行预测的数据10行
Xzhou = XX[0:10,0]
Xpre = X[0:10]
yreal = y[0:10]

# #############################################################################
# Fit regression model
# svr_rbf = SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, gamma='auto', kernel='rbf',
#   max_iter=-1, shrinking=True,
#   tol=0.001, verbose=False)
svr_lin = SVR(kernel='linear', C=1e3)
# svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbfm = svr_lin.fit(X, y)
joblib.dump(y_rbfm, "train_model.m")
y_rbf= y_rbfm.predict(Xpre)
# y_linmodel = svr_lin.fit(X, y)
# y_lin = y_linmodel.predict(Xpre)
# y_poly = svr_poly.fit(X, y).predict(Xpre)

# #############################################################################
# Look at the results
lw = 2
plt.scatter(Xzhou, yreal, color='darkorange', label='data')
plt.plot(Xzhou, y_rbf, color='navy', lw=lw, label='RBF model')
# plt.plot(Xzhou, y_lin, color='c', lw=lw, label='Linear model')
# plt.plot(Xzhou, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()