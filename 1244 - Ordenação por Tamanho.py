import sys


def tam_palavra(item):
    return len(item)


caseTeste = int(sys.stdin.readline())

for i in range(caseTeste):
    texto = sys.stdin.readline().split()
    texto = sorted(texto, key=tam_palavra, reverse=True)
    print(' '.join(texto))
