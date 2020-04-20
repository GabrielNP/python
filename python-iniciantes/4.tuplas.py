# Sequências => strings, listas, range, tupla
# Sequências imutáveis = Tuplas, range, string

dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
type(dias)

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

# Array/lista de tuplas
p1 = (1,2)
p2 = (2,3)
p3 = (3,4)
coordenadas = [p1, p2, p3]

person1 = ("Fulano", 39)
person2 = ("Beltrano", 25)
person3 = ("Ciclano", 42)
people = [person1, person2, person3]
people[1][0]


#  Converter LISTA em TUPLA
lista = [1,2,"gabriel"]
lista
tuplas2 = tuple(lista)
tuplas2

linhas = []
type(linhas)
linhas.append("linha 1")
linhas.append("linha 2")
linhas.append("linha 3")
linhas_tuple = tuple(linhas)
type(linhas_tuple)

# Converter TUPLA em LISTA
linhas_list = list(linhas_tuple)
type(linhas_list)
print(linhas_list)