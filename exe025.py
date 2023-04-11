v = float(input('Digite a velocidade do carro:'))
multa = (v - 80) * 7
if v > 80:
    print('Você foi multado em R${} reais'.format(multa))
else:
    print('Não deu em nada, RELAXA! Vai na fé')
