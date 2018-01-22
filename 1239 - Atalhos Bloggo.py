import sys
while True:
    try:
        palavra = list(input())
        cont = 0
        italico = 0
        negrito = 0
        for x in palavra:
            if x == "_" and italico == 0:
                italico += 1
                palavra[cont] = "<i>"
            elif x == "_" and italico == 1:
                italico -= 1
                palavra[cont] = "</i>"
            if x == "*" and negrito == 0:
                negrito += 1
                palavra[cont] = "<b>"
            elif x == "*" and negrito == 1:
                negrito -= 1
                palavra[cont] = "</b>"
            cont += 1
        sys.stdout.write(''.join(palavra)+'\n')
    except:
        break
