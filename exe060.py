print("---" * 20)
print("Sequência de Fibonacci")
print("---" * 20)
termo = int(input("Quantos termos você quer mostrar: "))
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2), end=' ')
cont = 3

while cont <= termo:
    t3 = t1 + t2
    print(" -> {}".format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print("Fim")
