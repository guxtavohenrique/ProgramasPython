viagem = float(input('Qual será a distância até seu destino(Km): '))
if viagem <= 200:
    print('O valor da passagem será de R${:.3f} reais'.format(viagem * 0.50))
else:
    print('O valor da passagem será de R${:.3f} reais'.format(viagem * 0.45))
