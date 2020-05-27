x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

# List Comprehension
# array = [valor_a_adicionar  laço  condição]

print("\n\n\nUsando list comprehension:\n")
z = [i**2 for i in x]
print(z)

# Exemplo com condição: imprimindo só os impares de x
g = [i for i in x if i%2==1]
print(g)


# Exemplo com função
def proximo_ano(idade):
    return idade + 1

idades = [20, 39, 18, 27, 19]
idade_ano_que_vem = [proximo_ano(idade) for idade in idades]
print(idade_ano_que_vem)