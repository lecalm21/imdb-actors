import http.client
import pandas as pd
import json

df = pd.read_csv('actorsBio.csv', usecols=[1])

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "58267bf279msh4dc691d9b335c4ep1f749fjsna540856ca553"
}

rows = []

for i, row in df.iterrows():

    conn.request(
        "GET", "/actors/get-all-filmography?nconst=" + row['NameID'], headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    pythonData = json.loads(data)
    print(pythonData.get('id').split('/')[2])
    print(pythonData.get('base').get('name'))
    print(pythonData.get('filmography'))
    rows.append([pythonData.get('id').split('/')[2],
                 pythonData.get('base').get('name'), pythonData.get('filmography')])


df = pd.DataFrame(rows)
df.columns = ['NameID', 'Name', 'Filmography']

df.to_csv('Filmography.csv', encoding='utf-8')


print(df)
