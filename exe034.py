print("--" * 20)
n = int(input("Digite um número inteiro: "))
print("--" * 20)

print("Escolha qual vai ser a base de conversão")
print("-=-" * 20)
print("-1 para binário")
print("-2 para octal")
print("-3 para hexadecimal")
print("-=-" * 20)

p = int(input("Escolha uma opção?: "))

if p == 1:
    print("Binário: {}".format(bin(n)[2:1]))
elif p == 2:
    print("Octal: {}".format(oct(n)[2:1]))
elif p == 3:
    print("Hexadecimal: {}".format(hex(n)[2:1]))
else:
    print("Nenhuma opção selecionada, rode o programa novamente!")
