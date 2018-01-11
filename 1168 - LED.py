i = int(input())
for x in range(i):
	led = 0
	n = input()
	for y in n:
		if y == "1":
			led += 2
		elif y == "2":
			led += 5
		elif y == "3":
			led += 5
		elif y == "4":
			led += 4
		elif y == "5":
			led += 5
		elif y == "6":
			led += 6
		elif y == "7":
			led += 3
		elif y == "8":
			led += 7
		elif y == "9":
			led += 6
		elif y == "0":
			led += 6
	print("%d leds" % led)