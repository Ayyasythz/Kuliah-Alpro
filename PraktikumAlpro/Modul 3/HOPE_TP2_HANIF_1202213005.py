angkaKali = int(input("Masukan angka yang ingin dikali: "))
lengKali = int(input("Sampai perkalian ke: "))

for x in range(1, lengKali + 1):
    print(f"{angkaKali} x {x} = {angkaKali * x}")
