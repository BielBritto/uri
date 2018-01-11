import sys
n = input().split()
n[0] = float(n[0])
n[1] = float(n[1])
n[2] = float(n[2])
print(["Otavio" if n[0] < n[1] and n[0] < n[2] else "Bruno" if n[1] < n[0] and n[1] < n[2] else "Ian" if n[2] < n[1] and n[2] < n[0] else "Empate"][0])