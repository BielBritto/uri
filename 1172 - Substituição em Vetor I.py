lista = []
cont = 0
for i in range(10):
	lista.append(int(input()))

for x in lista:
	if x < 1:
		print("X[%d] = 1" % cont)
		cont += 1
	else:
		print("X[%d] = %d" % (cont, x))
		cont += 1
