import sys
while True:
    i = int(sys.stdin.readline())
    if i == 0:
        break
    c1 = 0
    c2 = 0
    for x in range(i):
        a, b = list(map(int, sys.stdin.readline().split()))
        if a > b:
            c1 += 1
        elif b > a:
            c2 += 1
    print("{} {}".format(c1, c2))

