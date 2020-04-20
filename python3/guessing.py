# -*-coding:utf-8-*-
import random

def play():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Variáveis
    numero_secreto = random.randrange(1,101)
    rodada = 1
    pontos = 1000

    # Definição do nível da partida
    nivel = int(input("\n(1) Fácil (2) Médio (3) Difícil\nQual nível de dificuldade? R: "))
    while (nivel < 1 or nivel> 3):
        nivel = int(input("\n(1) Fácil (2) Médio (3) Difícil\nVocê deve escolher de 1 a 3 R: "))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    tentativas_restantes = total_tentativas

    # Laço de execução das partidas
    for rodada in range(1,total_tentativas +1):
        
        # Entrada de dado
        print("\n\n **** Rodada {} de {} ****".format(rodada,total_tentativas))
        chute = input("\nAdvinhe o seu número (entre 1 e 100): ")
        chute = int(chute)
        
        # Controle de dado
        while (chute < 1 or chute > 100):
            print("\nVocê deve digitar um número entre 1 e 100!")
            chute = input("\nAdvinhe seu número (entre 1 e 100): ")
            chute = int(chute)
        
        print("\nVocê digitou: ", chute)

            
        # Variáveis
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        # Processamento e saída de dado
        if (acertou):
            print("\nVOCÊ ADIVINHOU! PARABÉNS!\nSua pontuação foi", pontos)
            break
        else:
            print("\nVOCÊ ERROU!")
            if (maior):
                print("O seu chute foi MAIOR que o número secreto!")
            else:
                print("O seu chute foi MENOR do que o número secreto!")
            # Cálculo de pontos
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        

        # Contagem de tentativas
        tentativas_restantes = tentativas_restantes -1
        print("\nTentativas restantes:", tentativas_restantes)


    print("\n\n*********************************")
    print("Fim do jogo")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()