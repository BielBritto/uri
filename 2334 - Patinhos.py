import sys
while True:
    totPatos = int(sys.stdin.readline())
    if totPatos == -1: break

    print([totPatos-1 if totPatos > 0 else totPatos][0])
