tempo = int(input())
a, b = list(map(int, input().split()))

if a + b > tempo:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")