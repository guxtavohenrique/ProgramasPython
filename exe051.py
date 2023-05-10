import datetime
tma = 0
tme = 0
hoje = datetime.date.today().year
for c in range(1, 8):
    n = int(input("Digite o ano de nascimento da {} pessoa:(Ex:2000): ".format(c)))
    idade = hoje - n
    if idade >= 21:
        tma += 1
    elif idade <= 21:
        tme += 1
print("-=-" * 6)
print("Temos {} pessoas maiores de idade".format(tma))
print("Temos {} pessoas menores de idade".format(tme))
