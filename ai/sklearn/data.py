import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1000, size=(2000,5)), columns=['A', 'B', 'C', 'D', 'E'])
df['target'] = df.apply(lambda x: x['A']*x['A'] - 2 * x['B']+x['C']*x['D'], axis=1)  

df.to_csv('polyline.csv')