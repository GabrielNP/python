# -*-coding:utf-8-*-
import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    # Abrindo o arquivo de palavras
    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip() # Elimina espaços em branco, quebra de linha
        palavras.append(linha)
    
    arquivo.close()


    # Escolhendo uma das opções
    numero = random.randrange(0, len(palavras))
    

    # Declaração de variáveis
    palavra_secreta = palavras[numero].upper();
    enforcou = False
    acertou = False
    erros = 0
    
    letras_acertadas = ["_" for letra in palavra_secreta]
    print("\n\n",letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("\n\nQual letra? R: ")
        # Elimina os espaços em branco
        chute = chute.strip().upper()

        if (chute in palavra_secreta):                    
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erros += 1
            print("Não tem a letra \"{}\"".format(chute))
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        if (acertou):
            print("\nVocê ganhou!")
        elif (enforcou):
            print("\nVocê perdeu!")


    print("\n\n*********************************")
    print("Fim do jogo")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()