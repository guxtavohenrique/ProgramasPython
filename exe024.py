from random import choice
lista = [0, 1, 2, 3, 4, 5]
computador = choice(lista)
usuario = int(input('Escolha entre 0 a 5: '))
if usuario == computador:
    print('O computador pensou no número {} e você em {}, você acertou'.format(computador, usuario))
else:
    print('O computador pensou no número {} e você em {}, você errou'.format(computador, usuario))
print('Tente novamente')
