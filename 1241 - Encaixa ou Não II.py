n = int(input())
for i in range(n):
    x = input().split()
    a, b = x
    cont = a.find(b)
    print(["encaixa" if a == b else "encaixa" if cont > 0 and b[-1] == a[-1] else "nao encaixa"][0])
