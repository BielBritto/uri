lista = []
n = int(input())
for x in range(1, 10001):
	if x % n == 2:
		lista.append(x)

print('\n'.join(map(str, lista)))