from collections import deque

while True:

	cartas = int(input())
	if cartas == 0:
		break
	
	cartas = range(1, cartas + 1)
	cartas = deque(cartas)
	lista = []

	while len(cartas) != 1:
		lista.append(cartas.popleft())
		cartas.append(cartas[0])
		cartas.popleft()

	print("Discarded cards:", ', '.join(map(str, lista)))
	print("Remaining card: %d" % cartas[0])