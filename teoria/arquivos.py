# -*- coding: utf-8 -*-
# Abrir arquivos

# open(nome, modo)

#    Modos:
#       r   somente leitura
#       w/w+   escrita
#       a   leitura/escrita + novo conteúdo
#       r+  leitura/arquivo
#       a+  escrita + abre para atualização


# Ler

# read() --> lê arquivo todo
# readline() --> lê uma linha
# readlines() --> lê arquivo e armazena em lista

arquivo = open("README.md", "r")
print("1 ", arquivo)

linhas = arquivo.readlines()
print("2 ",linhas)
for linha in linhas:
    print("3 ",linha)

arquivo.close()

arquivo = open("README.md", "r")

texto_completo = arquivo.read()
print("4 ", texto_completo)

arquivo.close()


# Criar um arquivo
w = open("arquivo.txt", "w")
w.write("Esse é meu arquivo\n")
w.close()

w = open("arquivo.txt", "a")
w.write("Esse TAMBÉM é meu arquivo")
w.close()