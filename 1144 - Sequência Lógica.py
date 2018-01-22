from sys import stdin, stdout
n = int(stdin.readline())
for i in range(1, n+1):
    stdout.write("{:d} {:d} {:d}\n".format(i, i*i, i*i*i))
    stdout.write("{:d} {:d} {:d}\n".format(i, i*i+1, i*i*i+1))