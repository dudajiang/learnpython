from __future__ import print_function

import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

print('dudajiang')

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())

california_housing_dataframe["median_house_value"] /= 1000.0

# Define the input feature: total_rooms.
my_feature = california_housing_dataframe[["total_rooms"]]
my_feature2 = california_housing_dataframe["total_rooms"]

# # Configure a numeric feature column for total_rooms.
# feature_columns = [tf.feature_column.numeric_column("total_rooms")]

# targets = california_housing_dataframe["median_house_value"]

features = {key:np.array(value) for key,value in dict(my_feature).items()} 