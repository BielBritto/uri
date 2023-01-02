while True:
	try:
		entrada = list(input())
		left = 0
		right = 0
		open = 0

		for x in entrada:
			if x == '(':
				left += 1
			elif x == ')':
				right += 1
				if left > 0:
					left -= 1
					right -= 1
				else:
					open = 1

		print(['correct' if left == 0 and right == 0 and open == 0 else 'incorrect'][0])
	except:
		break
