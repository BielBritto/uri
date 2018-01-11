while True:
    try:
        qtdTest = input()
        if qtdTest == "0":
            break
        a = [int(x) for x in input().split()]
        b = set()
        [b.remove(x) if x in b else b.add(x) for x in a]        
        print(list(b)[0])

    except:
        break