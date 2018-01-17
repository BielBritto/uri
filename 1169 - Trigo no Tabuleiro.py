from math import pow
i = int(input())
for x in range(i):
    x = int(input())
    print("{:0.0f} kg".format(pow(2, x)//12000))
