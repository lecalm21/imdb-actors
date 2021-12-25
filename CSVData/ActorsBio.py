import http.client
import pandas as pd
import json
bio = {"@type": "imdb.api.name.bio", "id": "/name/nm2794962/", "image": {"height": 1200, "id": "/name/nm2794962/images/rm3989024257", "url": "https://m.media-amazon.com/images/M/MV5BMGFmZDVhZDUtZWIyNC00NzBjLTg0ZGEtY2FhMjJlZWJhZjBlXkEyXkFqcGdeQXVyMTcwNzE4OTI@._V1_.jpg", "width": 1200}, "name": "Hailee Steinfeld", "birthDate": "1996-12-11", "birthPlace": "Tarzana, Los Angeles, California, USA", "gender": "female", "heightCentimeters": 172.72, "realName": "Hailee Puring Steinfeld", "miniBios": [{"author": "Jaehun Han", "id": "/name/nm2794962/bio/mb0118268", "language": "en",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "text": "Hailee Steinfeld was born on December 11, 1996 in Tarzana, California, to Cheri (Domasin), an interior designer, and Peter Steinfeld, a personal fitness trainer. She has a brother, Griffin. Her uncle is Jake Steinfeld, a fitness trainer, and her great-uncle is actor Larry Domasin. Her father is of Ashkenazi Jewish descent and her mother\'s ancestry is Filipino, African-American, British Isles, and German. Hailee was raised in Thousand Oaks, California.\\n\\nAt an early age, she appeared in several short films to gain experience. She played the role of Talia Alden in She\'s a Fox (2009), which received several awards. Her debut in a feature film for theater was True Grit (2010). She played a major role, Mattie Ross, with Jeff Bridges, Josh Brolin, and Matt Damon. She got big attention for her performance in this movie, and she was nominated for the \'Best Supporting Actress\' Academy Award. After a short break, she appeared in several films which were released in 2013. She played the role of Juliet in Shakespeare\'s Romeo and Juliet (2013), which also starred Douglas Booth, and was released in 2013. Also, she appeared in Ender\'s Game (2013) as Petra Arkanian, based on the book written by Orson Scott Card, and this movie was directed by Gavin Hood. She starred with Asa Butterfield and Harrison Ford, and this movie received positive reviews. She appeared in the short film The Magic Bracelet (2013), with Bailee Madison, as Angela.\\n\\nIn 2014, She appeared in 3 Days to Kill (2014), which was released on February 21, 2014. she played the major role of Zoey Renner, daughter of Kevin Costner. In Hateship Loveship (2013), she played Sabitha with Kristen Wiig. This movie was released on April 11, 2014 in USA. Steinfeld performed the role of Emily Junk in Pitch Perfect 2 (2015). She also starred in Barely Lethal (2015) with Jessica Alba. She filmed the movie, Ten Thousand Saints (2015), as the role of Eliza, again opposite Asa Butterfield.\\n\\nIn 2016, she starred in the teen dramedy The Edge of Seventeen (2016), for which she received a Golden Globe nomination for Best Actress in a Motion Picture - Comedy or Musical.\\n\\nShe has been home-schooled since 2008. Hailee says she is very interested to be on the other side of camera and would like to eventually produce and direct.", "userId": "/user/ur2560386/"}]},

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "58267bf279msh4dc691d9b335c4ep1f749fjsna540856ca553"
}

actors = ["/name/nm2794962/", "/name/nm4427331/", "/name/nm2180812/", "/name/nm5085683/", "/name/nm0683253/", "/name/nm0369513/", "/name/nm1869101/", "/name/nm4141252/", "/name/nm0792263/", "/name/nm2933757/", "/name/nm5709125/", "/name/nm4689420/", "/name/nm0267812/", "/name/nm6073955/", "/name/nm1307435/", "/name/nm0687146/", "/name/nm3480246/", "/name/nm0717709/", "/name/nm1940449/", "/name/nm3918035/", "/name/nm4855517/", "/name/nm0158626/", "/name/nm0005351/", "/name/nm3154303/", "/name/nm4413036/", "/name/nm5377144/", "/name/nm0272581/", "/name/nm2244205/", "/name/nm0000631/", "/name/nm0000601/", "/name/nm0480869/", "/name/nm0425005/", "/name/nm5057169/", "/name/nm0198366/", "/name/nm0424060/", "/name/nm5896355/", "/name/nm5136993/", "/name/nm2400045/", "/name/nm1296458/", "/name/nm0719637/", "/name/nm2886648/", "/name/nm3031063/", "/name/nm4960279/", "/name/nm2024644/", "/name/nm1227814/", "/name/nm5939164/", "/name/nm3069650/", "/name/nm2093766/", "/name/nm0224565/", "/name/nm8808118/",
          "/name/nm0185819/", "/name/nm3381295/", "/name/nm0396558/", "/name/nm3078932/", "/name/nm0362766/", "/name/nm0000138/", "/name/nm3512758/", "/name/nm0111639/", "/name/nm3382410/", "/name/nm1212722/", "/name/nm6406427/", "/name/nm1102577/", "/name/nm1247407/", "/name/nm0001467/", "/name/nm1289434/", "/name/nm3485845/", "/name/nm1821446/", "/name/nm0540441/", "/name/nm4043618/", "/name/nm0000158/", "/name/nm1275259/", "/name/nm2080328/", "/name/nm8908475/", "/name/nm0000206/", "/name/nm0004802/", "/name/nm0000379/", "/name/nm2655177/", "/name/nm1017334/", "/name/nm2225369/", "/name/nm1931742/", "/name/nm0281448/", "/name/nm1195855/", "/name/nm0000226/", "/name/nm0748620/", "/name/nm0000707/", "/name/nm1556320/", "/name/nm6442992/", "/name/nm0405103/", "/name/nm2665105/", "/name/nm0000706/", "/name/nm1312575/", "/name/nm4555381/", "/name/nm8616975/", "/name/nm4422686/", "/name/nm0405281/", "/name/nm2088803/", "/name/nm0989182/", "/name/nm4317622/", "/name/nm0484916/", "/name/nm3099754/"]

rows = []

for x in range(50):
    nameID = actors[x].split("/")

    conn.request("GET", "/actors/get-bio?nconst=" +
                 nameID[2], headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    pythonData = json.loads(data)

    rows.append([pythonData.get('id').split('/')[2], pythonData.get('image').get('url'), pythonData.get('name'),
                pythonData.get('gender'), pythonData.get('heightCentimeters'),
                pythonData.get('birthDate'),
                pythonData.get('birthPlace'), pythonData.get('miniBios')[0].get('text')])

df = pd.DataFrame(rows)
df.columns = ['NameID', 'Image', 'Name', 'Gender',
              'Height', 'BirthDate', 'BirthPlace', 'Bios']

df.to_csv('actorsBio.csv', encoding='utf-8')


print(df)
