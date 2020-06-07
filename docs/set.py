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
# print(conjunto[1]


# ---------------------------------------------------------------------------------------------------------------------

usuarios_data_science = {15,23,43,56}
usuarios_machine_learning = {13,23, 56, 42}

# Tipo de dados: conjunto
print(type(usuarios_data_science))

# União dos conjuntos (equivalente à função extend() das listas)
print(usuarios_data_science | usuarios_machine_learning)

# Intersecção de conjuntos
print(usuarios_machine_learning & usuarios_data_science)
