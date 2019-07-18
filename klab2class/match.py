
# coding: utf-8

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.model_selection import cross_validate, GridSearchCV

train_data = pd.read_csv('./train_set.csv')
test_data = pd.read_csv('./test_set.csv')
train_data.drop(['ID'], axis=1, inplace=True)
test_data.drop(['ID'], axis=1, inplace=True)

# 将day和month去除
train_data.drop(['day'], axis=1, inplace=True)
test_data.drop(['day'], axis=1, inplace=True)
train_data.drop(['month'], axis=1, inplace=True)
test_data.drop(['month'], axis=1, inplace=True)

#train_data分成两个部分，一部分为训练集，一部分为测试集，拆分的原则是拆分后y的正负值比例相同
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(train_data, train_data["y"]):
    strat_train_set = train_data.loc[train_index]
    strat_test_set = train_data.loc[test_index]


train_x = strat_train_set.drop("y", axis=1) # drop labels for training set
train_y_labels = strat_train_set["y"].copy()
test_x = strat_test_set.drop("y", axis=1) # drop labels for training set
test_y_labels = strat_test_set["y"].copy()

try:
    from sklearn.impute import SimpleImputer # Scikit-Learn 0.20+
except ImportError:
    from sklearn.preprocessing import Imputer as SimpleImputer
    
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# 先将数值型的类型和文本型的类型选择出来
# num 就是中选择那些数值型的字段的dataframe
# train_x_num = train_data.drop('job', axis=1)  #选择多列
train_x_num = train_x.select_dtypes(include=[np.number]) #按照类型选择
train_x_text = train_x.select_dtypes(exclude=[np.number])

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler()),
    ])

train_num_tr = num_pipeline.fit_transform(train_x_num)


from sklearn.preprocessing import OneHotEncoder
try:
    from sklearn.compose import ColumnTransformer
except ImportError:
    from future_encoders import ColumnTransformer

num_attribs = list(train_x_num)
cat_attribs = list(train_x_text)

full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

train_x_prepared = full_pipeline.fit_transform(train_x)
test_x_prepared = full_pipeline.fit_transform(test_x)


f = open("out.txt", "w")  

gbm0 = GradientBoostingClassifier(random_state=11)
gbm0.fit(train_x_prepared, train_y_labels)


test_y_pred = gbm0.predict(test_x_prepared)
test_y_predprob = gbm0.predict_proba(test_x_prepared)
test_y_predprob = test_y_predprob[:, 1]

print("Accuracy : %.4g" % metrics.accuracy_score(test_y_labels, test_y_pred), file = f)
print("AUC Score (Train): %f" % metrics.roc_auc_score(test_y_labels, test_y_predprob), file = f)



train_y_pred = gbm0.predict(train_x_prepared)
train_y_predprob = gbm0.predict_proba(train_x_prepared)
train_y_predprob = train_y_predprob[:, 1]

print("Accuracy : %.4g" % metrics.accuracy_score(train_y_labels, train_y_pred))
print("AUC Score (Train): %f" % metrics.roc_auc_score(train_y_labels, train_y_predprob))



# param_test1 = {'n_estimators': range(20, 101, 10)}
# gbm1 = GradientBoostingClassifier(learning_rate=0.1, min_samples_split=1300,
#                                   min_samples_leaf=70, max_depth=7,subsample=0.8, random_state=11)

# gsearch1 = GridSearchCV(estimator=gbm1, param_grid=param_test1, scoring='roc_auc', iid=False, cv=5)
# gsearch1.fit(train_x_prepared, train_y_labels)
# print(gsearch1.cv_results_['mean_test_score'],
#       gsearch1.best_params_, gsearch1.best_score_)


# # In[ ]:


# param_test2 = {'n_estimators': range(20, 101, 10),
#               }
param_test2 = {'n_estimators': range(80, 101, 10),
               'max_depth': range(3, 22, 2),
               'min_samples_split': range(100, 1901, 200)
            #    'min_samples_leaf': range(60, 101, 10),
            #    'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9]
              }              
gbm2 = GradientBoostingClassifier(learning_rate=0.1, random_state=11)
gsearch2 = GridSearchCV(estimator=gbm2, param_grid=param_test2, scoring='roc_auc', iid=False, cv=5)
gsearch2.fit(train_x_prepared, train_y_labels)
print(gsearch2.cv_results_['mean_test_score'],
      gsearch2.best_params_, gsearch2.best_score_, file = f)

f.close()