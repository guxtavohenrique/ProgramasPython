nome = str(input('Digite seu nome completo:'))
d = nome.split()
print('maiúscula: {}'.format(nome.upper()))
print('minúsculo: {}'.format(nome.lower()))
print('seu nome tem: {} letras'.format(len(nome) - nome.count(' ')))
print('possui: {} letras'.format(len(d[0])))


