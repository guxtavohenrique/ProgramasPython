palavra = str(input("Digite uma frase: ")).lower().strip()
s = palavra.split()
j = ''.join(palavra)
i = ''
for l in range(len(j) - 1, -1, -1):
    i += j[l]
if i == j:
    print("Palíndromo")
else:
    print("Não é uma Palíndromo")
