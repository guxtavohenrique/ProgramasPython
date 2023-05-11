n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Média:{}'.format(m))
if m <= 5.0:
    print('Reprovado')
else:
    print('Aprovado')
print('--FIM--')
