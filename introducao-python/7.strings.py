# -*- coding: utf-8 -*-
a = "gabriel"
b = "novaes"

print(a + b)

concatenar = a + " " + b
print(concatenar)

tamanho = len(concatenar)
print(tamanho)

print(a[0])
print(a[1])
print(a[2])
print(concatenar[0:10])


# STRINGS SÃO OBJETOS
print(concatenar.lower())
print(concatenar.upper())

# .strip --> remover caracteres especiais e espaços
# .split --> converte sequencia em array

lista = "O rato roeu a roupa do rei de Roma"
busca = lista.find("rei")

# .replace()
