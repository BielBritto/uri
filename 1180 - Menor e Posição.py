input()
lista = list(map(int, input().split()))
pos = lista.index(min(lista))
print("Menor valor: %d\nPosicao: %d" % (min(lista), pos))