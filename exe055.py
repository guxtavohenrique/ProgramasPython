import random
palpites = 0

computador = random.randint(0, 10)
usuario = 0

print("-=-" * 20)
print("Bem vindo ao jogo de advinhação")
print("-=-" * 20)
while usuario != computador:
    print("O computador pensou em um número, tente advinhar...")
    usuario = int(input('Tente advinhar o número, tecle de 0-10: '))
    print("-=-" * 20)
    if usuario == computador:
        palpites += 1
        print("-=-" * 20)
        print("Parabéns você acertou.\nVocê precisou de {} tentativas!".format(palpites))
        print("-=-" * 20)
    else:
        print("{} Palpite :: Você errou, tente novamente.".format(palpites))
        print("-=-" * 20)
        palpites += 1
