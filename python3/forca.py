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
            print("Não tem a letra \"{}\"".format(attempt))
            print("Ops, você errou! Faltam {} tentativas.".format(6-errors))

        hanged = errors == 6
        won = "_" not in correct_chars

    if (won):
        victory_message()
    elif (hanged):
        game_over_message()

    end()


def welcome():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")


def load_secret_world():
    # Abrindo arquivo
    with open("palavras.txt","r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip() # Elimina espaços em branco, quebra de linha
            palavras.append(linha)
            
    # Escolhendo uma das opções
    numero = random.randrange(0, len(palavras))    
    
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


def victory_message():
    print("\nVocê ganhou!")


def game_over_message():
    print("\nVocê perdeu!")


def end():
    print("\n\n*********************************")
    print("Fim do jogo")
    print("*********************************")


if (__name__ == "__main__"):
    play()