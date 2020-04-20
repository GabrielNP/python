#  -*- coding: utf-8 -*-
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
    print('Desculpe, a {} não está na lista frutas'.format( 
