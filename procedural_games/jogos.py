# -*-coding:utf-8-*-

import hangman
import guessing

def select_game():
    print("*********************************")
    print("Escolha o seu jogo")
    print("*********************************")

    jogo = int(input("(1) Forca (2) Adivinhação\nQual jogo?\nR: "))
    while (jogo < 1 or jogo> 2):
        jogo = int(input("\n(1) Forca (2) Adivinhação\nVocê deve escolher 1 ou 2.\nR: "))
    if (jogo == 1):
        hangman.play()
    else:
        guessing.play()

if (__name__ == "__main__"):
    select_game()