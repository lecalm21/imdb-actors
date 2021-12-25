import http.client
import pandas as pd

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "58267bf279msh4dc691d9b335c4ep1f749fjsna540856ca553"
}

conn.request(
    "GET", "/actors/list-most-popular-celebs?homeCountry=US&currentCountry=US&purchaseCountry=US", headers=headers)

res = conn.getresponse()
data = res.read()


result = ["/name/nm2794962/", "/name/nm4427331/", "/name/nm2180812/", "/name/nm5085683/", "/name/nm0683253/", "/name/nm0369513/", "/name/nm1869101/", "/name/nm4141252/", "/name/nm0792263/", "/name/nm2933757/", "/name/nm5709125/", "/name/nm4689420/", "/name/nm0267812/", "/name/nm6073955/", "/name/nm1307435/", "/name/nm0687146/", "/name/nm3480246/", "/name/nm0717709/", "/name/nm1940449/", "/name/nm3918035/", "/name/nm4855517/", "/name/nm0158626/", "/name/nm0005351/", "/name/nm3154303/", "/name/nm4413036/", "/name/nm5377144/", "/name/nm0272581/", "/name/nm2244205/", "/name/nm0000631/", "/name/nm0000601/", "/name/nm0480869/", "/name/nm0425005/", "/name/nm5057169/", "/name/nm0198366/", "/name/nm0424060/", "/name/nm5896355/", "/name/nm5136993/", "/name/nm2400045/", "/name/nm1296458/", "/name/nm0719637/", "/name/nm2886648/", "/name/nm3031063/", "/name/nm4960279/", "/name/nm2024644/", "/name/nm1227814/", "/name/nm5939164/", "/name/nm3069650/", "/name/nm2093766/", "/name/nm0224565/", "/name/nm8808118/",
          "/name/nm0185819/", "/name/nm3381295/", "/name/nm0396558/", "/name/nm3078932/", "/name/nm0362766/", "/name/nm0000138/", "/name/nm3512758/", "/name/nm0111639/", "/name/nm3382410/", "/name/nm1212722/", "/name/nm6406427/", "/name/nm1102577/", "/name/nm1247407/", "/name/nm0001467/", "/name/nm1289434/", "/name/nm3485845/", "/name/nm1821446/", "/name/nm0540441/", "/name/nm4043618/", "/name/nm0000158/", "/name/nm1275259/", "/name/nm2080328/", "/name/nm8908475/", "/name/nm0000206/", "/name/nm0004802/", "/name/nm0000379/", "/name/nm2655177/", "/name/nm1017334/", "/name/nm2225369/", "/name/nm1931742/", "/name/nm0281448/", "/name/nm1195855/", "/name/nm0000226/", "/name/nm0748620/", "/name/nm0000707/", "/name/nm1556320/", "/name/nm6442992/", "/name/nm0405103/", "/name/nm2665105/", "/name/nm0000706/", "/name/nm1312575/", "/name/nm4555381/", "/name/nm8616975/", "/name/nm4422686/", "/name/nm0405281/", "/name/nm2088803/", "/name/nm0989182/", "/name/nm4317622/", "/name/nm0484916/", "/name/nm3099754/"]

rows = []

#here I got the 50 most popular actors
for x in range(50):
    nameID = result[x].split("/")
    rows.append([nameID[2]])
    df = pd.DataFrame(rows)
