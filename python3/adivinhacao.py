# -*-coding:utf-8-*-
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
tentativas_restantes = total_tentativas
rodada = 1

for rodada in range(1,total_tentativas +1):
    
    print("\n\n **** Rodada {} de {} ****".format(rodada,total_tentativas))
    chute = input("\nAdvinhe o seu número: ")
    print("\nVocê digitou: ", chute)

    chute = int(chute)

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