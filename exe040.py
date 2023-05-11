print("------IMC------")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
print("------IMC------")
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do Peso: IMC = {:.1f}".format(imc))
elif imc <= 25:
    print("Peso Ideal: IMC = {:.1f}".format(imc))
elif imc <= 30:
    print("Sobrepeso: IMC = {:.1f}".format(imc))
elif imc <= 40:
    print("Obesidade: IMC = {:.1f}".format(imc))
elif imc > 40:
    print("Obesidade Mórbida: IMC = {:.1f}".format(imc))
