from random import shuffle
a1 = str(input('Diga o nome do 1 aluno:'))
a2 = str(input('Diga o nome do 2 aluno:'))
a3 = str(input('Diga o nome do 3 aluno:'))
a4 = str(input('Diga o nome do 4 aluno:'))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem será formada por {}'.format(lista))
