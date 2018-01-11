while True:
	try:
		n = list(map(int, input().split()))
		a,b,c = n

		if a == b and a != c:
			print("C")
		elif a == c and a != b:
			print("B")
		elif b == c and b != a:
			print("A")
		else:
			print("*")
	except:
		break