l1 = float(input('O comprimento da 1 linha: '))
l2 = float(input('O comprimento da 2 linha: '))
l3 = float(input('O comprimento da 3 linha: '))

if l1 == l2 == l3:
    print("TRIÂNGULO EQUILÁTERO")
elif l1 == l2 != l3 and l2 == l3 != l1 and l3 == l1 != l2:
    print("TRIÂNGULO ISÓSCELES")
elif l1 + l2 > l3 and l3 + l2 > l1 and l3 + l1 > l2:
    print("TRIÂNGULO ESCALENO")
else:
    print("Não forma um triângulo")
