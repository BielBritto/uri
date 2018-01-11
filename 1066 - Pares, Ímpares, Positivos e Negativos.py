totPar = 0
totImpar = 0
totPos = 0
totNeg = 0

for cont in range(0, 5):
    numero = int(input())
    if numero >= 1:
        totPos += 1
    elif numero <= -1:
        totNeg += 1
    if numero % 2 == 0:
        totPar += 1
    else:
        totImpar += 1
print("%d valor(es) par(es)" %totPar)
print("%d valor(es) impar(es)" %totImpar)
print("%d valor(es) positivo(s)" %totPos)
print("%d valor(es) negativo(s)" %totNeg)
