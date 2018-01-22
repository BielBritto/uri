from collections import deque
from sys import stdin, stdout
while True:
    cartas = int(stdin.readline())
    if cartas == 0:
        break

    cartas = deque(range(1, cartas + 1))
    lista = []

    while len(cartas) != 1:
        lista.append(cartas.popleft())
        cartas.append(cartas.popleft())

    stdout.write("Discarded cards: {}\n".format(', '.join(map(str, lista))))
    stdout.write("Remaining card: {}\n".format(cartas[0]))
