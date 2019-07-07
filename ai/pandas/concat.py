import numpy as np
import pandas as pd

def preprocess_features(california_housing_dataframe):
  selected_features = california_housing_dataframe[
    ["A",
     "B",
     "C"]]
  selected_target = california_housing_dataframe[
    ["D"]]
  processed_features = selected_features.copy()
  processed_target = selected_target.copy()
  # Create a synthetic feature.
  return processed_features,processed_target

df = pd.DataFrame(pd.read_excel('./0101.xlsx',header=0))
df = df.reindex(np.random.permutation(df.index))
train_features,train_target = preprocess_features(df.head(5))
print(df)

prob = ['E0','E1','E2','E3','E4']
probdf = pd.DataFrame(data = prob,columns=['E'])

result = pd.concat([train_features,train_target])