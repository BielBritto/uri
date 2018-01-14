totCase = int(input())
primos = [2, ]
for x in range(totCase):
    ehprimo = 0
    limite = int(input())
    for i in range(3, limite + 1):
        if i % i == 0:
            cont += 1
        if cont > 2:
            break
    if cont == 2:
        print("{} eh primo".format(n))
    else:
        print("{} nao eh primo".format(n))