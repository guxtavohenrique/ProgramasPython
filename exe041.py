produto = float(input("Valor do Produto: "))

print("Escolha a forma de pagamento")

print("1 - À VISTA DINHEIRO/CHEQUE")
print("2 - À VISTA NO CARTÃO")
print("3 - NO CARTÃO EM ATÉ 2X")
print("4 - NO CARTÃO EM ATÉ 3X")

opcao = float(input("ESCOLHA UMA OPÇÃO: "))

if opcao == 1:
    print("O preço será de {}".format(produto - (10 / 100)))
elif opcao == 2:
    print("O valor será de {}".format(produto - (5 / 100)))
elif opcao == 3:
    print("O valor será dividido em 2X e cada parcela será de {}".format(produto / 2))
elif opcao == 4:
    print("O valor será dividido em 3X e cada parcela será de {}".format((produto + 20 / 100) / 3))
