valSal = float(input())
impostoTot = 0

if valSal <= 2000.00:
    print("Isento")
elif valSal > 2000.00 and valSal <= 3000.00:
    valSal -= 2000.00
    valSal = valSal * 0.08
    print("R$ %0.2f" %valSal)
elif valSal > 3000.00 and valSal <= 4500.00:
    valSal -= 2000.00
    impostoTot = 1000.00 * 0.08
    valSal -= 1000
    impostoTot += valSal * 0.18
    print("R$ %0.2f" %impostoTot)
elif valSal > 4500.00:
    valSal -= 2000.00
    impostoTot = 1000.00 * 0.08
    valSal -= 1000.00
    impostoTot += 1500.00 * 0.18
    valSal -= 1500.00
    impostoTot += valSal * 0.28
    print("R$ %0.2f" %impostoTot)