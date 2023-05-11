s = 'F' or 'M'

while s == 'F' or s == 'M':
    s = str(input("Digite seu sexo[F/M]: ")).upper()
if s != 'F' or s != 'M':
    print("Inválido, digite novamente")
print("Fim")
