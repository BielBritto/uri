fibo = []
def fibonacci(n):
	a = 1
	b = 1
	fibo.append(0)
	for i in range(n-1):
		fibo.append(a)
		x = a
		a = b
		b = b + x

n = int(input())
fibonacci(n)
print(' '.join(map(str, fibo)))