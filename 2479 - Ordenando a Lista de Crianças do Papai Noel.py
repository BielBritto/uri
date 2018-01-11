import sys
totKids = int(sys.stdin.readline())
cri = []
crif = []
bom = 0
mal = 0
while totKids > 0:
    cri.append(input())
    totKids -= 1

for x in cri:
    if x[0] == "+":
        bom += 1
        crif.append(x[2:])
    elif x[0] == "-":
        mal += 1
        crif.append(x[2:])
crif.sort()
print('\n'.join(crif))
print("Se comportaram: %d | Nao se comportaram: %d" % (bom, mal))