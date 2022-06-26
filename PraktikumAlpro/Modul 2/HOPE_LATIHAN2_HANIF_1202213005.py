try:
    gaji = int(input("Masukan pendapatan anda dalam 1 bulan : "))

    if gaji < 2000000 :
        print("Anda mendapat kategori A")
    elif gaji in range(2000000, 4000001):
        print("Anda mendapat kategori B")
    elif gaji in range(4100000, 5000001):
        print("Anda mendapat kategori C")
    elif gaji in range(5100000, 7000001):
        print("Anda mendapat kategori D")
    else:
        print("Anda tidak mendapat Bantuan")
except ValueError:
    print("Masukan Nominal Angka Gaji!!!")
