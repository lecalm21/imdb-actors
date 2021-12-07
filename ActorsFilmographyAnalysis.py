import http.client
import pandas as pd
import json

df = pd.read_csv('Filmography.csv')


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "dca6ee1f03msh0c3ce2e83fdc853p1a5fd1jsnb03748240d4a"
}


rows = []

for i, row in df.iterrows():

    conn.request(
        "GET", "/title/get-overview-details?tconst=" + row['TitleID'], headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    print("Data: " + data)
    pythonData = json.loads(data)

    print(pythonData.get('genres')[0])
    if pythonData.get('ratings').get('canRate'):
        rows.append([row['NameID'], row['Name'], row['TitleID'], row['TitleName'],
                    pythonData.get('genres')[0], pythonData.get(
                        'ratings').get('rating'),
                    pythonData.get('title').get('year')])


df = pd.DataFrame(rows)
df.columns = ['NameID', 'Name', 'TitleID',
              'TitleName', 'Genre', 'Rating', 'Year']

print(df)

df.to_csv('FilmographyAnalysis.csv', encoding='utf-8')
