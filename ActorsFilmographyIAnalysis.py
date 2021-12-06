import pandas as pd
import json

df = pd.read_csv('Filmography.csv', usecols=[3])
print(df)

#dictionary = df.iloc[1].values[0][0]
# print(dictionary)
