def dobro(x):
    return x*2

valor = [2,5,4,7,9]
valor_dobrado = (map(dobro, valor))
print(list(valor_dobrado))