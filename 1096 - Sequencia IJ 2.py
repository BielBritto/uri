i = 1
j = 7
cont = 0
while True:
    print("I={} J={}".format(i, j))
    j -= 1
    cont += 1
    if i == 9 and cont == 3:
        break
    elif cont == 3:
        i += 2
        j = 7
        cont = 0