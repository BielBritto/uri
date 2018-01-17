#Tentando

import sys
lista = []
n = int(sys.stdin.readline())
for i in range(n):
    sys.stdin.readline()
    y = list(map(int, sys.stdin.readline().split()))
    y.sort()
    lista.append(' '.join(map(str, y)))

sys.stdout.write('\n'.join(lista)+'\n')