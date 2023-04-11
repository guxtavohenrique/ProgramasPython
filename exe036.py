from datetime import date

print("-=-" * 20)
print("ALISTAMENTO MILITAR")
print("-=-" * 20)

ano = int(input("Seu ano de nascimento: "))
hoje = date.today().year
idade = hoje - ano

if idade == 18:
    print("Você está no tempo de se alistar!")
elif idade < 18:
    anos_faltantes = 18 - idade
    print("Faltam", anos_faltantes, "anos para você se alistar.")
else:
    anos_passados = idade - 18
    print("Seu prazo para se alistar já passou", anos_passados, "ano(s).")
