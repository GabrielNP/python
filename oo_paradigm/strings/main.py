from classe import ExtratorArgumentosUrl

'''
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
argumento = "Gabriel Novaes"
'''

url = "moedaorigem=moedaDestino&moedaDestino=dolar"

argumentosUrl = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = argumentosUrl.extrai_argumentos()
print(f'Moeda origem: {moeda_origem}\nMoeda destino: {moeda_destino}')