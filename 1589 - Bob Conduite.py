import sys
i = int(input())
for x in range(i):
    r1, r2 = list(map(int, sys.stdin.readline().split()))
    print(r1+r2)