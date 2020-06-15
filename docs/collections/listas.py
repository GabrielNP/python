# Imprimir
print("Imprimir")
lista = ["abacaxi", "melancia", "abacate"]
print(lista)
lista2 = [1, 2, 3, 4, 5]
print(lista2, "\n---------------------------\n")


# Concatenar
print("Concatenar")
lista3 = lista + lista2
print(lista3)
lista4 = lista3 + [8.9, False]
print(lista4)
print(lista4[5], "\n---------------------------\n")


# Laço
print("Laço")
for item in lista4:
    print(item)

# Tamanho com len()
print("\n---------------------------\nFunção len()")
tamanho = len(lista4)
print("O tamanho da lista 4 é ", tamanho, "\n---------------------------\n")


# Adicinando elemento com append()
print("Adicionar um elemento ao final com append()")
lista4.append("limao")
print(lista4, "\n---------------------------\n")

# Verificando se um elemento está na lista
print("Verificando se um elemento está na lista")
if 7 in lista4:
    print("7 está na lista\n---------------------------\n")
else:
    print("7 não está na lista\n---------------------------\n")


# Remover um elemento
lista4.remove("limao")
print("Removendo um elemento\n", lista4)


# Removendo pela posição com del
print("\nRemovendo um ou mais itens da lista pela posição")
del lista4[2:]
print(lista4, "\n---------------------------\n")

# Declarando uma lista vazia
print("Declarando uma lista vazia")
lista5 = []
print(lista5)


# Ordenando uma lista
print("\n---------------------------\n", "Ordenando uma lista")
lista = [9,1,5,4,6,8,2]
lista_ordenada = lista
lista.sort()
print("\ncom o método sort():", lista) #Não retorna nada e altera a lista original

print("\ncom o método sorted():", sorted(lista_ordenada)) # Retorna a ordenação e não altera a lista original

# Decrescente
lista.sort(reverse=True)
print("\nem sentido decrescente com <lista>.sort(reversed=True): ", lista)
print("\nem sentido descrecente com sorted(<lista>, reversed=True)", sorted(lista_ordenada, reverse=True),
      "ou com reversed(sorted(<lista>))", list(reversed(sorted(lista_ordenada))))

# Inverter lista
lista.reverse()
print("\ninvertendo: ",lista)

# Contar ocorrências
print("\n---------------------------\n", "Contando ocorrências")
valores = [ 0, 0, 1, 2, 0, 3, 4]
print("Quantas vezes o valor 0 aparece na lista", valores, "?  R.:", valores.count(0))


# Retornar o índice de um determinado elemento 
print("\n---------------------------\n", "Retornando o índice de um determinado elemento")
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas, "\nÍndice do Morango: ", frutas.index('Morango'))

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format(fruta_buscada))

# Array
print("\n---------------------------\n", "Array")
lista = [1, 2, 3, "gabriel", 5, 1]
print(lista)

# Incluir novo elemento na lista
lista.append("python")
lista.append(20)
print(lista)


# Método extend
print("\n---------------------------\nInserindo uma lista de elementos dentro de outra lista")
print("Lista 1", lista, "\nLista 3:", lista3)
lista.extend(lista3)
print("Lista 3 dentro de Lista 1:", lista)