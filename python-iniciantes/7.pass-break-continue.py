# BREAK
numero = 21

while True:
    print(numero)
    numero=numero-1
    if(numero==2):
        break


# CONTINUE
num = 12
while True:
    print(num)
    num=num-1
    if(num==4):
            continue
    print("banana")
    if(num==2):
        break

# PASS
for x in range(0,5):
    print(x)
        pass
