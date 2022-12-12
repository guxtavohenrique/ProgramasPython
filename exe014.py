from math import cos, sin, tan, radians
angulo = float(input('Digite um ângulo:'))
print('O seno é {:.2f}'.format(sin(radians(angulo))))
print('O cosseno é {:.2f}'.format(cos(radians(angulo))))
print('A tangente é {:.2f}'.format(tan(radians(angulo))))
