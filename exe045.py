n = int(input("Escolha um número: "))
print("-=-" * 6)
print("Tabuada do {}".format(n))
print("-=-" * 6)
for t in range(0, 11):
    print("{} X {:2} = {:2}".format(n, t, t*n))
print("-=-" * 6)
print("Fim")
