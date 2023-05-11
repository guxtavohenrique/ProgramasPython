from random import randint

lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print("==" * 20)
print("[ 0 ] Pedra")
print("[ 1 ] Papel")
print("[ 2 ] Tesoura")
print("==" * 20)

usuario = int(input("Escolha: "))

print("==" * 20)
print("O computador escolheu {}".format(lista[computador]))
print("Você escolheu {}".format(lista[usuario]))
print("==" * 20)

if computador == 0 and usuario == 0:
    print("Empate")
elif computador == 0 and usuario == 1:
    print("Jogador Venceu")
elif computador == 0 and usuario == 2:
    print("Computador Venceu")

if computador == 1 and usuario == 0:
    print("Computador Venceu")
elif computador == 1 and usuario == 1:
    print("Empate")
elif computador == 1 and usuario == 2:
    print("Jogador Venceu")

if computador == 2 and usuario == 0:
    print("Jogador Venceu")
elif computador == 2 and usuario == 1:
    print("Computador Venceu")
elif computador == 2 and usuario == 2:
    print("Empate")

else:
    print("Inválido")
