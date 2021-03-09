"""
To index each element of a list.
Returns a list of tuples (index, element)
"""

list1 = ["apple", "ball", "dog"]

# manual way to index each element of list1
for i in range(len(list1)):
    print(i, list1[i])
    # 0 apple
    # 1 ball
    # 2 dog 

# with enumerate() method
for index, name in enumerate(list1):
    print(index, name)
    # 0 apple
    # 1 ball
    # 2 dog 

# -------------------------------------------------------------------

ages = [15, 87, 32, 65, 56, 32, 49, 37]

print(ages)
print(range(len(ages)))

enumerate(ages)
print(list(range(len(ages))))  # forçando a geração de uma lista de valores
print(list(enumerate(ages)))  #obtendo em tuplas os pares de indice e idade

for value in enumerate(ages): # retorno empacotado do método enumerated
    print (value)

for index, age in enumerate(ages): # desempacotando as tuplas
    print(index, age)


#
users = [
    ("Guilherme", 37, 1991),
    ("Daniala", 31, 1995),
    ("Paula", 29, 1996)
]

for name, age, birthday in users:  # já desempacotando
    print(name)
for name, _, _, in users:  # já desempacotando ignorando os demais elementos
    print(name)