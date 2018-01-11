import sys
lenFila = int(sys.stdin.readline())

fila = [x for x in sys.stdin.readline().split()]

totSaida = int(sys.stdin.readline())
sairam = [x for x in sys.stdin.readline().split()]
pos = 0
cont = 0

while totSaida > 0:
	pos = fila.index(sairam[cont])
	del(fila[pos])

	cont += 1
	totSaida -= 1

print(' '.join(fila))