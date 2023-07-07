print("Loja do Seu Zé")
print("---" * 10)
total = mil = cont = menor = barato = 0
while True:
    nome = str(input("Nome do produto: ")).strip().lower()
    preco = float(input("Preço: R$ "))
    cont += 1
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input("Continuar[S/N]: ")).strip().lower()[0]
    print("---" * 10)
    if preco != 0:
        total += preco
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if pergunta == 'n':
        print(f"Gasto Total: {total}")
        print(f"Produtos que custam mais que R$1.000: {mil}")
        print(f"Nome do produto mais barato: {barato}")
        break
