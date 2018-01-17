import sys
while True:
    n = int(sys.stdin.readline())
    if n < 1:
        break
    sys.stdout.write(' '.join(map(str, list(range(1, n+1)))) + "\n")