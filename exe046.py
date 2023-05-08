n = int(input("Digite um número: "))
print("-=-" * 5)
for t in range(0, 11):
    print("{:2} X {} = {:2}".format(t, n, t*n))
print("-=-" * 3)
print("Fim")
