# -*-coding:utf-8-*-
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(int(random.random() * 100))
total_tentativas = 3
tentativas_restantes = total_tentativas
rodada = 1

for rodada in range(1,total_tentativas +1):
    
    print("\n\n **** Rodada {} de {} ****".format(rodada,total_tentativas))
    chute = input("\nAdvinhe o seu número (entre 1 e 100): ")
    chute = int(chute)
    
    while (chute < 1 or chute > 100):
        print("\nVocê deve digitar um número entre 1 e 100!")
        chute = input("\nAdvinhe seu número (entre 1 e 100): ")
        chute = int(chute)
    
    print("\nVocê digitou: ", chute)

        

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("\nVOCÊ ADIVINHOU! PARABÉNS!")
        break
    else:
        print("\nVOCÊ ERROU!")
        if (maior):
            print("O seu chute foi MAIOR que o número secreto!")
        else:
            print("O seu chute foi MENOR do que o número secreto!")
        
    tentativas_restantes = tentativas_restantes -1
    print("\nTentativas restantes: ",tentativas_restantes)


print("\n\n*********************************")
print("Fim do jogo")
print("*********************************")