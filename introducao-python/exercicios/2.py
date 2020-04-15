# Faça um programa que receba duas notas digitadas pelo usuário. 
# Se a média for maior ou igual a seis, escreva aprovado. se não, escreva reprovado.   

nota = input("Digite uma nota: ")
nota = int(nota)

nota2 = input("Digite outra nota: ")
nota2 = int(nota2)

media = (nota + nota2)/2

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")