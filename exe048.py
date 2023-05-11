n = int(input("Verificar número: "))
mult = 0

for count in range(2, n):
    if (n % count == 0):
        print("Multiplo de", count)
        mult += 1

    if (mult == 0):
        print("É primo")
    else:
        print("Tem", mult, "multiplos acima de 2 e abaixo de", n)
