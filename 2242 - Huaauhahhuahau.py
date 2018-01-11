n = input()
vog = []
vogr = []
for x in n:
	if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
		vog.append(x)
		vogr.append(x)

vogr.reverse()
vog = ''.join(vog)
vogr = ''.join(vogr)
if vog == vogr:
	print("S")
else:
	print("N")