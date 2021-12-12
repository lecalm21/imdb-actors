import urllib.request
import pandas as pd


df = pd.read_csv('./CSVData/ActorsBio.csv')
print(df)
        
rows = []
for i, row in df.iterrows():
    row['Image']
    urllib.request.urlretrieve(row['Image'], "./ImagesActors/"+ row['NameID'] + ".jpg")