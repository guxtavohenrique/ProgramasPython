l1 = float(input('O comprimento da 1 linha: '))
l2 = float(input('O comprimento da 2 linha: '))
l3 = float(input('O comprimento da 3 linha: '))
if l1 + l2 > l3 or l1 == l2 == l3 or l1 == l2 != l3:
    print('Forma um TRIÂNGULO')
else:
    print('Não forma um TRIÂNGULO')
