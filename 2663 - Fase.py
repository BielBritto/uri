import sys
totComp = int(sys.stdin.readline())
notas = []
totClass = int(sys.stdin.readline())
for x in range(totComp):
	notas.append(int(sys.stdin.readline()))
notas.sort(reverse=True)
qtdClass = 0
cont = 0
esimo = 0

for x in notas:
		
	if totClass > 0:
		qtdClass += 1
		esimo = x
	elif x == esimo:
		qtdClass += 1
	
	cont += 1
	totClass -= 1
	
print(qtdClass)

