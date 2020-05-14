# -*- coding: utf-8 -*-
a = "gabriel"
b = "novaes"


# concatenando string
print(a + b)
concatenar = a + " " + b
print(concatenar)


# método len
tamanho = len(concatenar)
print("O texto tem",tamanho,"caracteres")


# substring, fatiando strings
print("0 ->", concatenar[0])
print("1 ->", concatenar[1])
print("2 ->", concatenar[2])
print("10->",concatenar[10])
print(concatenar[2:10])


# STRINGS SÃO OBJETOS -> podem acessar funções da classe string
print("minusculo ->",concatenar.lower())
print("maiusculo ->",concatenar.upper())


# método find()
lista = "O rato roeu a roupa do rei de Roma"
busca = lista.find("rei")
print(busca)


# .strip --> remover caracteres especiais e espaços iniciais/finais
print("concatenar =", "  $%" + concatenar + "@")
print("com strip",concatenar.strip())


# .split --> converte sequencia em array
texto = "a * b *c * d * 1 * 2"
print(texto.split("*"))


# none e empty
eh_none = None
eh_vazio = ""

if eh_none is None:
    print("Variavel é", type(eh_none))
if eh_vazio:
    print("Tem alguma coisa aqui")
else:
    print("Variavel é", type(eh_vazio))


# .replace()
print(lista.replace("do rei", "da rainha"))