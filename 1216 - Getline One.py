import sys
cont = 0
dist = 0
while True:
    try:
        sys.stdin.readline()
        dist += float(sys.stdin.readline())
        cont += 1
    except:
        break
print("{:0.1f}".format(dist / cont))