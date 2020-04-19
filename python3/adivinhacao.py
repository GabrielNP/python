# -*-coding:utf-8-*-
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("\nAdvinhe o seu número: ")
print("\nVocê digitou: ", chute)

chute = int(chute)

if chute == numero_secreto:
    print("\nVOCÊ ADIVINHOU! PARABÉNS!")
else:
    print("\nVOCÊ ERROU!")

print("\n\nFim do jogo")