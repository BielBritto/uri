import sys
n = sys.stdin.readline()
if n[0] == "-":
	n = float(n)
	print("%.4E" % n)
else:
	n = float(n)
	print("+%.4E" % n)