print("------IMC------")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do Peso: {:2f}".format(imc))
elif imc <= 25:
    print("Peso Ideal: {:2f}".format(imc))
elif imc <= 30:
    print("Sobrepeso: {:2f}".format(imc))
elif imc <= 40:
    print("Obesidade: {:2f}".format(imc))
elif imc > 40:
    print("Obesidade Mórbida: {:2f}".format(imc))
