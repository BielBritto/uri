totCases = int(input())
while totCases > 0:
	cont = 0
	cifra = list(input())
	chave = int(input())
	
	for x in cifra:
		cifra[cont] = ord(x)
		cifra[cont] -= chave
		if cifra[cont] < 65:
			cifra[cont] += 26
		cifra[cont] = chr(cifra[cont])
		cont += 1

	cifra = ''.join(cifra)
	print(cifra)
	totCases -= 1