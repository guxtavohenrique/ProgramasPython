print('=='*50)
print('----------------CONVERSOR DE TEMPERATURA----------------')
print('=='*50)
temperatura = float(input('Digite a temperatura em ºC:'))
c = (temperatura * 9/5) + 32
print('A temperatura de {}ºC, corresponde a {:.1f}ºF!'.format(temperatura, c))
