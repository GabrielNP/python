from classe import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedaDestino&moedaDestino=dolar&valor=700"

argumentosUrl = ExtratorArgumentosUrl(url)

moeda_origem, moeda_destino = argumentosUrl.extrai_argumentos()
valor = argumentosUrl.extrai_valor()

print(f'Moeda origem: {moeda_origem}\nMoeda destino: {moeda_destino}\nValor: {valor}')