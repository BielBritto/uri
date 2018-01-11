qtdIngress = 5
teste = 0
while qtdIngress != 0:

    qtdIngress = int(input())
    nesimo = 0
    cont = 1
    teste += 1

    if qtdIngress == 0:
        break;

    numIngress = [int(x) for x in input().split(" ")]

    for x in numIngress:
        if x == cont and nesimo == 0:
            nesimo = x
        cont += 1

    print("Teste %d"%teste + "\n%d"%nesimo + "\n")