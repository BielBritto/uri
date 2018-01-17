n = int(input())
for i in range(n):
    cont = 0
    comida = float(input())
    while comida > 1:
        cont += 1
        comida /= 2
    print("{} dias".format(cont))
