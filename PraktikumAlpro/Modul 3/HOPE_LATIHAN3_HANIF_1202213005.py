list = []
awal = int(input("Awal: "))
akhir = int(input("Akhir: "))
deret = ""
for x in range(awal,akhir+1):
    if x != akhir:
        deret += " " + str(x * (3 * x - 2))
    else:
        print(f"Deret bilangan :{deret}")








