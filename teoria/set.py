# Set = Conjuntos, ou seja, cada elemento da lista é único

cpf1 = 111
cpf2 = 222
cpf3 = 333

conjunto = {cpf1,cpf2,cpf3}
print(conjunto)

cpf4 = 333
conjunto.add(cpf4)
# o set ignorou essa adição, pois um mesmo elemento já existe
print(conjunto)


# Não possui índice
print(conjunto[1])