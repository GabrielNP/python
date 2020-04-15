lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i, lista[i])


# Enumerate
print("\n\nUsando função enumerate")

for i,nome in enumerate(lista):
    print(i,nome)