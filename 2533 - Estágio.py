from sys import stdin, stdout
while True:
    try:
        n = 0
        c = 0
        d = 0
        e = 0
        t = int(stdin.readline())
        for i in range(t):
            n, c = list(map(int, stdin.readline().split()))
            d+= n*c
            e += c
        e *= 100
        stdout.write("{:0.4f}\n".format(d/e))
    except:
        break
