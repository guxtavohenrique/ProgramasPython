from math import hypot
print('HIPOTENUSA')
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
print('A hipotenusa de {} e {} é igual:{:.2f}'.format(co, ca, hypot(co, ca)))
