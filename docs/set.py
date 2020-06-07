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

A = {15,23,43,56}
B = {13,23, 56, 42}
print(f"A: {A}\nB: {B}")

# Tipo de dados: conjunto
print(type(A))

# União dos conjuntos (equivalente à função extend() das listas)
print("União:",  A | B)

# Intersecção de conjuntos
print("Intersecção: ", B & A)

# Operações com conjuntos
print("Está contido em B, mas não em A:", B - A)
print("Está contido em A, mas não em B:", A - B)

print("XOR = ou está só no A ou só no B:", A ^ B)
