lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i, lista[i])

print("\n\nUsando função enumerate")

for indice, nome in enumerate(lista):
    print(indice, nome)


# -------------------------------------------------------------------
idades = [15, 87, 32, 65, 56, 32, 49, 37]
print(idades)
print(range(len(idades)))
print (enumerate(idades))
print(list(range(len(idades))))  # forçando a geração de uma lista de valores
print(list(enumerate(idades)))  #obtendo em tuplas os pares de indice e idade

for valor in enumerate(idades): # retorno empacotado do método enumerated
    print (valor)

for indice, idade in enumerate(idades): # desempacotando as tuplas
    print(indice, idade)


#
usuarios = [
    ("Guilherme", 37, 1991),
    ("Daniala", 31, 1995),
    ("Paula", 29, 1996)
]

for nome, idade, nascimento in usuarios:  # já desempacotando
    print(nome)
for nome, _, _, in usuarios:  # já desempacotando ignorando os demais elementos
    print(nome)