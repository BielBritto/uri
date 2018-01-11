pino = list(input().split())
entrada = list(input().split())

cont = 0
n = 0

while cont < len(pino):
	if pino[cont] == entrada[cont]:
		break
	else:
		n += 1
	cont += 1

print(["Y" if n == 5 else "N"][0])