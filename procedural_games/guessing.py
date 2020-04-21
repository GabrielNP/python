# -*-coding:utf-8-*-
import random


def play():
    
    welcome()

    secret_number = number_generator()

    match_round = 1
    score = 1000

    total_attempts = select_level()
    attempts_left = total_attempts

    for match_round in range(1,total_attempts +1):        
        
        attempt = request_attempt(match_round, total_attempts)
        
        won = attempt == secret_number
        bigger = attempt > secret_number
        menor = attempt < secret_number

        
        if (won):
            victory_message(score)
            break
        else:
            wrong_choice(bigger)
            score = lost_points(secret_number,attempt, score)
            attempts_left = attempt_count(attempts_left)

        if (match_round == total_attempts):
            game_over_message(secret_number)

    end()


def welcome():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


def number_generator():
    return random.randrange(1,101)


def select_level():
    level = int(input("\n(1) Fácil (2) Médio (3) Difícil\nQual nível de dificuldade? R: "))
    total_attempts = 0

    while (level < 1 or level> 3):
        level = int(input("\n(1) Fácil (2) Médio (3) Difícil\nVocê deve escolher de 1 a 3 R: "))

    if (level == 1):
        total_attempts = 20
    elif (level == 2):
        total_attempts = 10
    else:
        total_attempts = 5
    
    return total_attempts


def request_attempt(match_round, total_attempts):
    print("\n\n **** Rodada {} de {} ****".format(match_round,total_attempts))
    attempt = int(input("\nAdvinhe o seu número (entre 1 e 100): "))

    while (attempt < 1 or attempt > 100):
        print("\nVocê deve digitar um número entre 1 e 100!")
        attempt = int(input("\nAdvinhe seu número (entre 1 e 100): "))
    
    print("\nVocê digitou: ", attempt)
    return attempt
    

def victory_message(score):
    print("\nVOCÊ ADIVINHOU! PARABÉNS!\nSua pontuação foi", score)


def wrong_choice(bigger):
    print("\nVOCÊ ERROU!")
    if (bigger):
        print("O seu chute foi MAIOR que o número secreto!")
    else:
        print("O seu chute foi MENOR do que o número secreto!")


def lost_points(secret_number, attempt, score):
    lost_points = abs(secret_number - attempt)
    return score - lost_points


def attempt_count(attempt):
    attempt = attempt -1
    print("\nTentativas restantes:", attempt)
    return attempt


def game_over_message(number):
    print("\nPuxa, você foi perdeu! O número era {}".format(number))
    print("\n    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("/\/                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def end():
    print("\n\n*******************************")
    print("\tFim do jogo")
    print("*******************************")


if (__name__ == "__main__"):
    play()