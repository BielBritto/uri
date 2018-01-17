import sys
while True:
    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 0 and n[1] == 0:
        break
    else:
        print("{}".format(n[0] + n[1]))