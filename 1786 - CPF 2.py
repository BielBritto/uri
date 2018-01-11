while True:
    try:
        cpf = input()
        cpf = list(cpf)
        cpf = list(map(int, cpf))

        cpf.append(((cpf[0] * 1) + (cpf[1] * 2) + (cpf[2] * 3) + (cpf[3] * 4) + (cpf[4] * 5) + (cpf[5] * 6) + (cpf[6] * 7) + (cpf[7] * 8) + (cpf[8] * 9)))
        cpf[9] = (cpf[9] % 11)

        if cpf[9] >= 10:
            cpf[9] = 0
        cpf.append(((cpf[0] * 9) + (cpf[1] * 8) + (cpf[2] * 7) + (cpf[3] * 6) + (cpf[4] * 5) + (cpf[5] * 4) + (cpf[6] * 3) + (cpf[7] * 2) + (cpf[8] * 1)))
        cpf[10] = cpf[10] % 11
        if cpf[10] >= 10:
            cpf[10] = 0


        print("%d%d%d.%d%d%d.%d%d%d-%d%d" % (cpf[0], cpf[1], cpf[2], cpf[3], cpf[4], cpf[5], cpf[6], cpf[7], cpf[8], cpf[9], cpf[10]))
    except:
        break