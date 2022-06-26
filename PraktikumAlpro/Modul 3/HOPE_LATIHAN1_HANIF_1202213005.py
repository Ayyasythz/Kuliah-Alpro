bilPertama = int(input("Bilangan Pertama : "))
bilTerkahir = int(input("Bilangan Terkahir : "))

for x in range(bilPertama,bilTerkahir+1):
    if x % 2 == 0:
        print(f"Bilangan ke-{x} adalah genap")
    elif x % 2 != 0:
        print(f"Bilangan ke-{x} adalah ganjil")