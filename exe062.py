print("Maior, menor e média")
cont = soma = media = maior = menor = 0
escolha = 'S'

while escolha != 'N':
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = str(input("Deseja continuar[S/N]: ")).upper().strip()
media = soma / cont
print("Você digitou {} números e a média entre eles é {}".format(cont, media))
print("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}".format(menor))
print("FIM")
