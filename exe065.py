from random import choice
cont = 1
escolha = ['par', 'impar']

while True:
    usuario = str(input("Digite 'Par' ou 'Impar': ")).upper().strip()
    computador = choice(escolha).upper().strip()
    print("***" * 20)
    if usuario != computador:
        print("Tente novamente")
        cont += 1
        print("***" * 20)
    else:
        print(f"Vocẽ precisou de {cont} vezes para ganhar!")
        print("***" * 20)
        break
