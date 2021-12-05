import pandas as pd
df = pd.read_csv('actorsBio.csv', sep='\t')
print(df.iloc[1, 0])
# print(df)
