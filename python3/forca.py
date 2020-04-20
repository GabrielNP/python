# -*-coding:utf-8-*-
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana";    
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    print(letras_acertadas)

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual letra? R: ")
        # Elimina os espaços em branco
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)



    print("\n\n*********************************")
    print("Fim do jogo")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()