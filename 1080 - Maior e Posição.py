pos = 0
nMaior = 0
lista = []
for x in range(1, 101):
	n = int(input())
	
	if nMaior < n:
		nMaior = n
		pos = x

print("{}\n{}".format(nMaior, pos))