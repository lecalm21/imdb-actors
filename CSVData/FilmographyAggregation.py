import pandas as pd

film1 = pd.read_csv('FilmographyAnalysis1.csv', usecols=['NameID', 'Name', 'TitleID','TitleName', 'Genre', 'Rating', 'Year'])
film2 = pd.read_csv('FilmographyAnalysis2.csv', usecols=['NameID', 'Name', 'TitleID','TitleName', 'Genre', 'Rating', 'Year'])
film3 = pd.read_csv('FilmographyAnalysis3.csv', usecols=['NameID', 'Name', 'TitleID','TitleName', 'Genre', 'Rating', 'Year'])
film4 = pd.read_csv('FilmographyAnalysis4.csv', usecols=['NameID', 'Name', 'TitleID','TitleName', 'Genre', 'Rating', 'Year'])




rows = []

for i, row in film1.iterrows():

    rows.append(row)

for i, row in film2.iterrows():

    rows.append(row)

for i, row in film3.iterrows():

    rows.append(row)

for i, row in film4.iterrows():

    rows.append(row)


df = pd.DataFrame(rows)
df.columns = ['NameID', 'Name', 'TitleID',
              'TitleName', 'Genre', 'Rating', 'Year']


df.to_csv('FilmographyAnalysis.csv', encoding='utf-8')

df = pd.read_csv('FilmographyAnalysis.csv', usecols=['NameID', 'Name', 'TitleID','TitleName', 'Genre', 'Rating', 'Year'])


#here I aggregated the different filmography items into one csv 
#because the api couldn´t handle all the request with one account
for i, row in df.iterrows():

    rows.append(row)

df = pd.DataFrame(rows)
df.columns = ['NameID', 'Name', 'TitleID',
              'TitleName', 'Genre', 'Rating', 'Year']

df.to_csv('FilmographyAnalysis.csv', encoding='utf-8')