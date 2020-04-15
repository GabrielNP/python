
def pares(i):
    if i % 2 == 0:
        return i


lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares,lista)
print(lista_pares)
print(list(lista_pares))

# list para converter o objeto lista_pares em array