# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   

numero = input("Digite um numero: ")
numero = int(numero)

numero2 = input("Digite outro numero: ")
numero2 = int(numero2)

operador = input("Digite um operador matemático:\n1 +\n2 -\n3 *\n4 / ")
operador = int(operador)

if (operador == 1):
    print(numero + numero2)
elif (operador == 2):
    print(numero - numero2)
elif (operador == 3):
    print(numero * numero2)
else:
    print(numero / numero2)


