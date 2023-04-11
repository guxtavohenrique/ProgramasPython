import random

lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)

print(computador)

usuario = str(input("Escolha entre (PEDRA, PAPEL E TESOURA: "))

if computador == 'pedra' and usuario == 'pedra':
    print("Empate")
elif computador == 'pedra' and usuario == 'papel':
    print("O computador perdeu")
elif computador == 'pedra' and usuario == 'tesoura':
    print("O computador ganhou")

elif computador == 'papel' and usuario == 'papel':
    print("Empate")
elif computador == 'papel' and usuario == 'tesoura':
    print("O computador perdeu")
elif computador == 'papel' and usuario == 'pedra':
    print("O computador ganhou")

elif computador == 'tesoura' and usuario == 'tesoura':
    print("Empate")
elif computador == 'tesoura' and usuario == 'papel':
    print("O computador ganhou")
elif computador == 'tesoura' and usuario == 'pedra':
    print("O computador perdeu")
