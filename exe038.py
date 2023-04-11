import datetime

dia = int(input("Seu dia de aniversário (DD): "))
mes = int(input("Seu mês de aniversário (MM): "))
ano = int(input("Seu ano de aniversário (AAAA): "))

dt_nascimento = datetime.date(ano, mes, dia)

hoje = datetime.date.today()
idade = hoje.year - dt_nascimento.year - ((hoje.month, hoje.day) < (dt_nascimento.month, dt_nascimento.day))

if idade <= 9:
    print("MIRIM", idade)
elif idade <= 14:
    print("INFANTIL", idade)
elif idade <= 19:
    print("JUNIOR", idade)
elif idade <= 25:
    print("SÊNIOR", idade)
else:
    print("MASTER", idade)
