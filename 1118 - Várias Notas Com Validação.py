import sys
while True:
    while True:
        n1 = float(sys.stdin.readline())
        if n1 >= 0 and n1 <= 10:
            break
        sys.stdout.write("nota invalida\n")
    while True:
        n2 = float(sys.stdin.readline())
        if n2 >= 0 and n2 <= 10:
            break
        sys.stdout.write("nota invalida\n")
    print("media = {:0.2f}".format((n1+n2)/2))
    while True:
        x = input("novo calculo (1-sim 2-nao)\n")
        if x == "1" or x == "2":
            break
    if x == "2":
        break
