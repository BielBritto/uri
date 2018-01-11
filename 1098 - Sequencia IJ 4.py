for I in range(0, 21, 2):
	for J in range(1, 4):
		I2 = I/10
		if I2 == int(I2):
			print("I=%d J=%d" % (I2, I2 + J))
		else:
			print("I=%.1f J=%.1f" % (I2, I2 + J))