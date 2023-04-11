print("----MÉDIA ESCOLAR----")
nota_1 = float(input("DIGITE SUA PRIMEIRA NOTA: "))
nota_2 = float(input("DIGITE SUA SEGUNDA NOTA: "))
print("--" * 10)
media = (nota_1 + nota_2) / 2

if media >= 7.0:
    print("APROVADO", media)
elif media >= 5.0:
    print("RECUPERAÇÃO", media)
else:
    print("REPROVADO", media)
