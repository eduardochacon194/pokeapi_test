import requests
#import json

res = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')

with open("public/new_pokes.json", "w") as  Parse_json:
    Parse_json.write(res.text)
    Parse_json.close() 

""" with open("public/new_pokes.json", "r") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

poke = jsonObject['results'][1]['name']
poke = jsonObject['results']
print (len(poke))
 """