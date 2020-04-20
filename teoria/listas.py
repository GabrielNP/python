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

# Ordenando
lista = [135,35468,864,1815,321,0]
lista_ordenada = lista

lista.sort()
print(lista)

lista_ordenada = sorted(lista)
print(lista_ordenada)

# Decrescente
lista.sort(reverse=True)
print(lista)

# Inverter lista
lista.reverse()
print(lista)

# Contar ocorrências
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))

# Retornar o índice de um determinado elemento 
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Uva'))
fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format(fruta_buscada))

# Array
lista = [1,2,3,"gabriel",5,1]
print(lista)

# Incluir novo elemento na lista
lista.append("python")
lista.append(20)
print(lista)

# Saber a posição de um elemento na lista
lista.index("gabriel")

# Contar a ocorrência de elementos
lista.count(1)

# Remover um elemento
lista.remove("python")

# Inverter ordem da lista
lista.reverse()

# Ordenar uma lista
lista2 = [4,2,98,7,2,6,7,5]
print(lista2)
lista.sort()