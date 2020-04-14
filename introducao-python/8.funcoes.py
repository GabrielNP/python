# -*- coding: utf-8 -*-

# DEFINIÇÃO:
# def NOME(PARAMETROS):
#   COMANDOS

# CHAMADA:
# NOME(ARGUMENTOS)

def soma(x,y):
    print(x + y)

soma(2,3)

# ----------------------------------------------

def soma(x,y):
    return x + y

s = soma(2,3)
print(s)

# ----------------------------------------------

def multiplicacao(x,y):
    return x * y

m = multiplicacao(2,3)
print(m)


print(soma(s,m))