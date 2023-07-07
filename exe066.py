print("---" * 5)
print("   BEM VINDO   ")
print("---" * 5)
cont = contm = masc = 0
while True:
    idade = int(input("Qual a sua idade: "))
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input("Qual é o seu sexo[F/M]: ")).strip().lower()[0]
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input("Quer continuar[S/N]: ")).strip().lower()[0]
    print("***" * 20)
    if idade > 18:
        cont += 1
    if idade < 20:
        contm += 1
    if sexo == 'm':
        masc += 1
    if pergunta == 'n':
        print(f"Tem {cont} com mais de 18 anos!")
        print(f"Tem {masc} homens cadastados!")
        print(f"Tem {contm} mulheres com menos de 20 anos!")
        break
