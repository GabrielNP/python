from classe import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedaDestino&moedaDestino=dolar&valor=700"

argumentosUrl = ExtratorArgumentosUrl(url)
print(len(argumentosUrl))
print(argumentosUrl)