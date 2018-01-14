lista = []
lista.append(int(input()))
cont = 0
for i in range(9):
    lista.append(lista[i]*2)

for i in lista:
    print("N[{}] = {}".format(cont, i))
    cont += 1