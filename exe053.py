maior = 0
menor = 0
soma_idade = 0
maior_homem = 0
nome_velho = ''
tmulher = 0
for c in range(1, 5):
    print("-=-=-= {} pessoa-=-=-=-".format(c))
    nome = str(input("Nome: "))
    idade = float(input("Idade: "))
    sexo = str(input("Sexo[M/F]: ")).lower()

    soma_idade += idade

    if c == 1 and sexo in 'Mm':
        maior_homem = idade
        nome_velho = nome
    if sexo in 'm' and idade > maior_homem:
        maior_homem = idade
        nome_velho = nome
    if sexo in 'f' and idade < 20:
        tmulher += 1

soma_idade = soma_idade / 4

print('-=' * 10)
print("A média de idade do grupo é de {}".format(soma_idade))
print("O homem mais velho do grupo é {}".format(nome_velho))
print("A quantidade de mulheres que tem menos de 20 anos é {}".format(tmulher))
