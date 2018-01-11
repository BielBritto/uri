while True:
	try:
		cont = 0
		x = 1
		n = int(input())
		if n == 1:
			print(0)
		else:
			while x < n:
				x = x * 2
				cont += 1

			print(cont)
	except:
		break