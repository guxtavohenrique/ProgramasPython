print('-=-' * 20)
print('EMPRÉSTIMO BANCÁRIO')
print('-=-' * 20)
casa = float(input('Qual é o valor da casa?: '))
salario = float(input('Qual é o seu salário atual?: '))
anos = int(input('Quantos anos pretende pagar?: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print("A prestação do imóvel será de: R${:.2f}".format(prestacao))
if prestacao <= minimo:
    print("Concedido")
else:
    print("Negado")
