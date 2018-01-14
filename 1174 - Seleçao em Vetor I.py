lista = []
cont = 0
for x in range(100):
    lista.append(float(input()))
for i in lista:
    if i <= 10:
        print("A[{}] = {:0.1f}".format(cont, i))
    cont += 1