# Set = Conjuntos, ou seja, cada elemento da lista é único
# É mutável.

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

# ---------------------------------------------------------------------------------------------------------------------

# Adicionando elementos ao conjunto (pois é mutável)
usuarios = {1,3,6,4,2,7}
usuarios.add(9)  # equivalente ao append() da lista
print(usuarios)

# Tornando o conjunto imutavel
usuarios2 = frozenset(usuarios)
print(type(usuarios2))
# usuarios2.add(10)  # vai dar erro, porque um dado tipo fronzenset não tem o atributo add(), ou seja, fronzenset é imutável
print(usuarios2)

# ---------------------------------------------------------------------------------------------------------------------
# Transformando lista em conjunto
meu_texto = "Oi meu nome é Gabriel e eu gosto de tocar piano eu tenho um piano"
novo_texto = meu_texto.split(" ")
print(novo_texto)
print(set(novo_texto))  # um conjunto a partir da lista existente. Foram removidos os elementos repetidos.
