import sys

def fat(n):
	if n <= 1:
		return 1
	else:
		return n * fat(n-1)

n = int(sys.stdin.readline())

print(fat(n))