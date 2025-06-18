num = float(input("Omonat miqdorini kiriting: "))

if num < 100_000:
    print("5%")
if 100_000 < num < 500_000:
    print("7%")
if num > 500_000:
    print("10%")        