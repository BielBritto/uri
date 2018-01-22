from sys import stdin, stdout
#Não resolvido
x = int(stdin.readline())
y = int(stdin.readline())
soma = 0
if x < y:
    for i in range(x+1, y-1):
        if i > 0:
            soma += i
else:
    for i in range(y+1, x-1):
        if i > 0:
            soma += i
print("{}".format(soma))