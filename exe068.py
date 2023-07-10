print("=" * 40)
print("{:^40}".format("BANCO AMERICANO"))
print("=" * 40)
sacar = int(input("Informe o valor a ser sacado| R$: "))
tot = sacar
cedula = 50
total = 0
while True:
    if tot >= cedula:
        tot -= cedula
        total += 1
    else:
        print(f"{total} cédulas de R$: {cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total = 0
        if tot == 0:
            break
