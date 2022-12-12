from random import choice
a1 = str(input('Diga o nome do 1 aluno(a): '))
a2 = str(input('Diga o nome do 2 aluno(a): '))
a3 = str(input('Diga o nome do 3 aluno(a): '))
a4 = str(input('Diga o nome do 4 aluno(a): '))
lista = [a1, a2, a3, a4]
print('O aluno(a) escolhido foi >>> {}'.format(choice(lista)))
