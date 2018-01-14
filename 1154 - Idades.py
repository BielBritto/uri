totIdades = 0
cont = 0
while True:
    n = int(input())
    if n < 0:
        break
    else:
        totIdades += n
        cont += 1
print("{:02.2f}".format(totIdades/cont))