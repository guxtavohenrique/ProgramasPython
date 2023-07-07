"""
import time

c = 0

while c != 11:
    time.sleep(0.8)
    print(c, end=' ')
    c += 1
print("Finished")
"""

'''
r = 'S'

while r == 'S':
    n = int(input("Digite um  número: "))
    r = str(input("Quer continuar[S/N]: ")).upper()
print("Finished")
'''

'''

n = 1
par = impar = 0

while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("{} pares e {} ímpares".format(par, impar))


'''