from math import factorial
num = 0
c = 'S'
while c == 'S':
    num = int(input("Digite qualquer valor para mostrar seu fatorial: "))
    if num == 0:
        print("O fatorial de {}! é igual a 1".format(num))
    if num == 1:
        print("O fatorial de {}! é igual a 1".format(num))
    if num != 0 and num != 1:
        print("-=-" * 10)
        print("O fatorial de {}! é igual a {}".format(num, factorial(num)))
        print("-=-" * 10)
    c = str(input("Quer continuar[S/N]?: ")).strip().upper()
    print("-=-" * 10)
print("FIM")
