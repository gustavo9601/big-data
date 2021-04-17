import pandas as pd
import numpy as np
import seaborn
import matplotlib
import sklearn

# cargamos nuestro dataset
df_wines = pd.read_csv('./databases/vinos_tintos.csv')
print(df_wines.shape)
print(df_wines.head())
