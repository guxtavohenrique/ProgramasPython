s = float(input('Digite eu salário: '))
if s >= 1250:
    print('Seu aumento será de R${:.2f} reais'.format((s * 0.10) + s))
else:
    print('Seu salário será de R${:.2f} reais'.format((s * 0.15) + s))
