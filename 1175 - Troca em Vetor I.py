lista1 = []
lista2 = []
for x in range(20):
	if x < 10:
		lista1.append(int(input()))
	else:
		lista2.append(int(input()))

lista1.reverse()
lista2.reverse()
lista2.extend(lista1)

for x in range(20):
	print("N[{}] = {}".format(x, lista2[x]))
