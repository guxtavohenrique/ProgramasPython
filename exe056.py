import time
escolha = 0
while escolha != 6:
    print("-=-" * 10)
    print("[ 1 ] somar")
    print("[ 2 ] dividir")
    print("[ 3 ] multiplicar")
    print("[ 4 ] maior")
    print("[ 5 ] novos valores")
    print("[ 6 ] sair do programa")
    print("-=-" * 10)
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    print("-=-" * 10)

    escolha = int(input("Escolha uma opção[1-6]: "))

    if escolha == 1:
        soma = n1 + n2
        print("A soma de {} + {} é igual a {}".format(n1, n2, soma))
    elif escolha == 2:
        dividir = n1 / n2
        print("A divisão entre {} / {}, resultou em {}".format(n1, n2, dividir))
    elif escolha == 3:
        multiplicar = n1 * n2
        print("A multiplicação entre {} * {}, resultou em {}".format(n1, n2, multiplicar))
    elif escolha == 4:
        if n1 > n2:
            print("{} é maior".format(n1))
        else:
            print("{} é maior".format(n2))
    elif escolha == 5:
        print("-=-" * 10)
        print("Novos Valores")
        n1 == n1
        n2 == n2
    elif escolha == 6:
        for t in range(5, -1, -1):
            print(t)
            time.sleep(0.5)
        print("Byebye.........")
    elif escolha != [1, 2, 3, 4, 5, 6]:
        print("Erro, tente novamente")
