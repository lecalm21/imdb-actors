import http.client
import pandas as pd
import json

df = pd.read_csv('Filmography3.csv')


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "8341b28612mshd563e1e9a378839p1e0d15jsnd8adbc1dea78"
}


rows = []


# here I get the information for each film in filmography csv and create a filmography analysis csv with the rating
for i, row in df.iterrows():

    conn.request(
        "GET", "/title/get-overview-details?tconst=" + row['TitleID'], headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    
    pythonData = json.loads(data)

    if pythonData.get('ratings').get('canRate'):
        rows.append([row['NameID'], row['Name'], row['TitleID'], row['TitleName'],
                    pythonData.get('genres')[0], pythonData.get(
                        'ratings').get('rating'),
                    pythonData.get('title').get('year')])


df = pd.DataFrame(rows)
df.columns = ['NameID', 'Name', 'TitleID',
              'TitleName', 'Genre', 'Rating', 'Year']

df.to_csv('FilmographyAnalysis3.csv', encoding='utf-8')
