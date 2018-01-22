import sys
caso = 0
while True:
    try:
        numSequencia = int(sys.stdin.readline())
        caso += 1
        totSequencia = [0, ]
        for cont in range(0, numSequencia + 1):

            for cont2 in range(0, cont):
                totSequencia.append(cont)
        tamanho = len(totSequencia)
        if len(totSequencia) == 1:
            sys.stdout.write("Caso {}: {} numero\n0\n\n".format(caso, tamanho))
        else:
            sys.stdout.write("Caso {}: {} numeros\n".format(caso, tamanho))
            sys.stdout.write(' '.join(map(str, totSequencia)) + '\n\n')
    except:
        break;