lista1 = [1,4,5,6,7]
lista2 = ["gato", "cao", "pato", "rato"]

for numero, nome in zip(lista1, lista2):
    print(numero, nome)


lista3 = [True, 5.6, "2.4", "barato", 2]


for numero, nome, coisa in zip(lista1, lista2, lista3):
    print(numero, nome, coisa)