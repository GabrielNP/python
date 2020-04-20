# Sequências => strings, listas, range, tupla
# Sequências imutáveis = Tuplas, range, string

dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
>>> type(dias)

tuplas=("gabriel","osvaldo","tadeu")
tuplas

tuplas[0:1]
tuplas[0:2]

# Verificar o tamanho
len(tuplas)

tuplas+tuplas
tuplas*5

4 in tuplas
"tadeu" in tuplas


#  Converter array em tupla
lista = [1,2,"gabriel"]
lista
tuplas2 = tuple(lista)
tuplas2