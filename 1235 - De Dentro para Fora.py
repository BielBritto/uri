totCases = int(input())
while totCases > 0:
    texto = list(input())
    texto.reverse()
    tamanho = len(texto)
    tamanho = tamanho // 2
    p2 = ''.join(texto[0:tamanho])
    p1 = ''.join(texto[tamanho:])

    print("%s%s" % (p1,p2))

    totCases -= 1
totCases = int(input())
while totCases > 0:
    texto = list(input())
    texto.reverse()
    tamanho = len(texto)
    tamanho = tamanho // 2
    p2 = ''.join(texto[0:tamanho])
    p1 = ''.join(texto[tamanho:])

    print("%s%s" % (p1,p2))

    totCases -= 1
