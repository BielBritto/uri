while True:
    try:
        texto = list(input())
        for i in range(len(texto)):
            if ord(texto[i]) >= 65 and ord(texto[i]) <= 90:
                if ord(texto[i]) + 13 > 90:
                    texto[i] = ord(chr(texto[i] - 25 + 13))
                else:
                    texto[i] = ord(chr(texto[i] + 13))
            elif ord(texto[i]) >= 97 and ord(texto[i]) <= 122:
                if ord(texto[i]) + 13 > 122:
                    texto[i] = ord(chr(texto[i] - 25 + 13))
                else:
                    texto[i] = ord(chr(texto[i] + 13))
        print(texto)
    except:
        break