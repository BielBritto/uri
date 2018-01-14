i = int(input())
inn = 0
out = 0
for x in range(i):
    n = int(input())
    if n >= 10 and n <= 20:
        inn += 1
    else:
        out += 1

print("{} in\n{} out".format(inn, out))