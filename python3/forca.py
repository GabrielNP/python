# -*-coding:utf-8-*-
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana";
    palavra_secreta.upper()

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual letra? R: ")
        # Elimina os espaços em branco
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra \"{}\" na posição {}".format(letra,index+1))
            index = index + 1

        print("\nJogando...")



    print("\n\n*********************************")
    print("Fim do jogo")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()