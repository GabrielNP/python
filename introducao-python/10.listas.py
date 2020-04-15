lista = ["abacaxi", "melancia", "abacate"]
print(lista)

lista2 = [1,2,3,4,5]
print(lista2)

lista3 = lista + lista2
print(lista3)

lista4 = lista3 + [8.9, False]
print(lista4)
print(lista4[5])

for item in lista4:
    print(item)

tamanho = len(lista4)
print("O tamanho da lista 4 é ", tamanho)

lista4.append("limao")
print(lista4)

if 7 in lista4:
    print("7 está na lista")
else:
    print("7 não está na lista")

del lista4[2:]
print(lista4)

lista5 = []
print(lista5)