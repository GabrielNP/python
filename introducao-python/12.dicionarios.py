# -*-coding:utf-8-*-
# Dicionários = array associativo, ou seja, um determinado valor passa a ser vinculado a uma chave.
# Ex: dicionario_sites = {"Diego": "diegomariano.com"}

dicionario = {
    "A":"Ameixa",
    "B":"Bola",
    "C":"Cachorro"
}

print(dicionario)

# Erro aqui
# print("Erro aqui: ", dicionario[0])

print(dicionario["A"])
print(dicionario["B"])
print(dicionario["C"])

for chave in dicionario:
    print(chave + ":" + dicionario[chave])

for i in dicionario.items():
    print(i)

for j in dicionario.values():
    print(j)

for z in dicionario.keys():
    print(z)