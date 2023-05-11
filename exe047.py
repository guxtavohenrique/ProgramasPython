s = 0
for n in range(1, 7):
    num = int(input("Digite o {} número: ".format(n)))
    if num % 2 == 0:
        s += num
print("A soma dos par(es) será de {}".format(s))
print("FIM")
