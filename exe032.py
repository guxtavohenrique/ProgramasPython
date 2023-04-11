n1 = int(input('Digite o 1 número: '))
n2 = int(input('Digite o 2 número: '))
n3 = int(input('Digite o 3 número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('-=-' * 20)
print('O menor número vai ser o {}'.format(menor))
print('O maior valor vai ser o {}'.format(maior))
print('-=-' * 20)
