i = 1
j = 7
cont = 0
while True:
    print("I={} J={}".format(i,j))
    j -= 1
    cont += 1
    if j > 11 and cont > 2:
        break
    if cont > 2:
        i += 2
        j += 5
        cont = 0