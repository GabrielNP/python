# -*-coding:utf-8-*-
# Dicionários = array associativo, ou seja, um determinado valor passa a ser vinculado a uma chave.
# São conjuntos (sets) de pares chave-valor
# Ex: dicionario_sites = {"Diego": "diegomariano.com"}

# ---------------------------------------------------------------------------------------------------------------------

# Formas de construir um dict
dicionario = {
    "A": "Ameixa",
    "B": "Bola",
    "C": "Cachorro"
}

dicionario2 = dict(A='Ameixa')

print(dicionario, dicionario2)
print(type(dicionario), type(dicionario2))

# ---------------------------------------------------------------------------------------------------------------------

# Erro aqui: Não existe posição em dicts. Caso existe alguma chave 0 em um dict ela deve ser acessada através de aspas
# print("Erro aqui: ", dicionario[0])

print(dicionario["A"])
print(dicionario["B"])
print(dicionario["C"])
# print(dicionario["D"]) --> Erro aqui: não existe esse elemento no conjunto.
# Existe um méotodo melhor para acessar os elementos.
print(dicionario.get("D", 0))  # Quando não tem, retorna zero.

# Técnicas de looping
# Imprimindo todos os elementos / chaves
for elementos in dicionario:
    print(elementos)

for z in dicionario.keys():
    print(z)

# Imprimindo os valores
for j in dicionario.values():
    print(j)

# Imprimindo os pares de chave:valor
for chave in dicionario:
    print(chave + ":" + dicionario[chave])

for i in dicionario.items():
    print(i)

# Desempacotando os pares
for chave, valor in dicionario.items():
    print(chave, "=", valor)

# ---------------------------------------------------------------------------------------------------------------------

telefones={"gabriel": 1197228521, "tadeu": 1197228522, "osvaldo": 1197228523}
print(telefones)

# Adicionar
telefones["rita"] = 11972228524
print(telefones)

# Remover
del telefones["tadeu"]
print(telefones)

# Verificar se um elemento está contido no conjunto
"gabriel" in telefones
"carlos" in telefones

# ---------------------------------------------------------------------------------------------------------------------

person1 = {"Fulano": 39}
person2 = {"Beltrano": 25}
person3 = {"Ciclano": 42}
print()
people = [person1, person2, person3]

person1["Beltrano"] = 25
person1["Ciclano"] = 42
print(person1['Fulano'])
