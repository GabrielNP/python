# -*-coding:utf-8-*-
import random

def play():

    welcome()
    secret_word = load_secret_world()
    correct_chars = current_word(secret_word)

    print("\n\n",correct_chars)    
   
    hanged = False
    won = False
    errors = 0
    
    while (not hanged and not won):

        attempt = request_attempt()

        if (attempt in secret_word):                    
            score(attempt, correct_chars, secret_word)
        else:
            errors += 1
            print("\nOps! O.O\nNão tem a letra \"{}\".\n\nFaltam {} tentativas.".format(attempt,7-errors))
            show_gallow(errors)

        hanged = errors == 7
        won = "_" not in correct_chars

    if (won):
        victory_message()
    elif (hanged):
        game_over_message(secret_word)

    end()


def welcome():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")


def load_secret_world(valid_line=0, file="frutas.txt"):
    # Abrindo arquivo
    with open(file,"r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip() # Elimina espaços em branco, quebra de linha
            palavras.append(linha)
            
    # Escolhendo uma das opções
    numero = random.randrange(valid_line, len(palavras))    
    
    # Definindo a palavra da partida
    palavra_secreta = palavras[numero].upper();
    return palavra_secreta
    

def current_word(palavra):
    return ["_" for letra in palavra]


def request_attempt():
    chute = input("\n\nQual letra? R: ")
    chute = chute.strip().upper()
    return chute


def score(attempt, chars, word):
    index = 0
    for char in word:
        if (attempt == char):
            chars[index] = char
        index += 1
    print(chars)


def show_gallow(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def victory_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def game_over_message(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
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
    print("\n\n*********************************")
    print("Fim do jogo")
    print("*********************************")


if (__name__ == "__main__"):
    play()