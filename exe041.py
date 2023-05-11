print("==" * 20)
produto = float(input("Valor do(s) Produto(s): "))
print("==" * 20)

print("Escolha a forma de pagamento")

print("[ 1 ] - À VISTA DINHEIRO/CHEQUE")
print("[ 2 ] - À VISTA NO CARTÃO")
print("[ 3 ] - NO CARTÃO EM ATÉ 2X")
print("[ 4 ] - 3X OU MAIS NO CARTÃO")

opcao = float(input("=>ESCOLHA UMA OPÇÃO: "))

if opcao == 1:
    print("O preço será de {:.2f}".format(produto - (produto * 10 / 100)))

elif opcao == 2:
    print("O valor será de {:.2f} no cartão".format(produto - (produto * 5 / 100)))

elif opcao == 3:
    print("O valor será dividido em 2X e cada parcela será de {:.2f}".format(produto / 2))

elif opcao == 4:
    print("==" * 20)
    escolha = int(input("Quantas vezes pretende dividi: "))

    total = produto + (produto * 20 / 100)

    print("==" * 20)
    print("O valor: =>{} será dividido em =>{}X e cada parcela "
          "será de =>{:.2f}".format(produto, escolha, total / escolha))
else:
    print("====>Opção Inválida!<====")
