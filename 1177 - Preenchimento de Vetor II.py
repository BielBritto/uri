n = int(input())
i = 0
for x in range(1000):
	print("N[{}] = {}".format(x, i))
	if i >= n-1:
		i = 0
	else:
		i += 1
