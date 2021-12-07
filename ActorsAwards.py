import http.client
import pandas as pd
import json

df = pd.read_csv('actorsBio.csv')


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "dca6ee1f03msh0c3ce2e83fdc853p1a5fd1jsnb03748240d4a"
}


rows = []

for i, row in df.iterrows():

    conn.request("GET", "/actors/get-awards?nconst=" +
                 row['NameID'], headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    pythonData = json.loads(data)
    awards = pythonData.get('awards')
    for x, award in awards:
        print(award[x])
        if award.get('titleType') == 'movie':
            rows.append([pythonData.get('id').split('/')[2],
                        pythonData.get('base').get(
                            'name'), award.get('id').split('/')[2],
                        award.get('title'), award.get('titleType')])


df = pd.DataFrame(rows)
df.columns = ['NameID', 'Name', 'TitleID', 'TitleName', 'TitleType']

df.to_csv('Filmography.csv', encoding='utf-8')
