for nome in range(0, 50):
    nome = str(input("Digite uma frase:")).upper()
    if nome == "".join(reversed(nome)):
        print("Palíndromo")
    else:
        print("Não é um Palíndromo")
print("Fim")
