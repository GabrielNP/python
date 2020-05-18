from classe import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedaDestino&moedaDestino=dolar&valor=700"

argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url)

print(len(argumentosUrl))

print(argumentosUrl, id(argumentosUrl),"\n-----------------------------------")
print(argumentosUrl2, id(argumentosUrl2))

print(argumentosUrl == argumentosUrl2)