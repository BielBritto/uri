import sys
teste = 0
while True:

    qtdIngress = input()
    nesimo = 0
    cont = 1
    teste += 1

    if qtdIngress == "0":
        break;

    numIngress = list(map(int, sys.stdin.readline().split()))

    for x in numIngress:
        if x == cont and nesimo == 0:
            nesimo = x
        cont += 1

    print("Teste {}\n{}\n".format(teste, nesimo))