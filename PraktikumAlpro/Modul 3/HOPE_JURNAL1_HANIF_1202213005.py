
baris = int(input("Masukan tinggi baris: "))

for x in range(0,baris+1):
    for y in range(x, baris):
        print(" ",end="")
    print("" * (baris - 1), "*", )