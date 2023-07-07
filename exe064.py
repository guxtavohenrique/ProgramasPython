while True:
    num = int(input("Digite um número[número negativo para parar]: "))
    if num < 0:
        break
    else:
        for cont in range(0, 11):
            print(f"{num} x {cont} = {num * cont}")
print("BYEBYE QUIRIDO")
