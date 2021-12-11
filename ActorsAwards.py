import http.client
import pandas as pd
import json

df = pd.read_csv('actorsBio.csv')


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "a1906b1576mshb1b515f46e72534p197b1cjsn9eb21f3e5bf3"
}


rows = []

for i, row in df.iterrows():

    conn.request("GET", "/actors/get-awards?nconst=" +
                 row['NameID'], headers=headers)

    print(row['NameID'])
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    pythonData = json.loads(data)
    awards = pythonData.get('resource').get('awards')
    #print(awards)
    if awards:
        for award in awards:
            print(award.get('awardName'))
            print(award.get('year'))
            
            rows.append([row['NameID'], award.get('awardName'), award.get('year')])


df = pd.DataFrame(rows)
df.columns = ['NameID', 'AwardName', 'Year']

df.to_csv('ActorsAwards.csv', encoding='utf-8')
