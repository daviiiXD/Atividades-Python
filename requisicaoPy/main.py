import requests
import json
arquivo = open('requisicaoPy/database.txt', 'w+')

listaGravar = []
listaLer = []

request = requests.get("https://fakestoreapi.com/products")
produtos = json.loads(request.content)#converte a resposta para uma lista de dicionários


for i in produtos:
     listaGravar.append(str(i['image']) + "\n")

for i in listaGravar:
     arquivo.write(i)

for i in listaLer:
     arquivo.read(i)                                                            