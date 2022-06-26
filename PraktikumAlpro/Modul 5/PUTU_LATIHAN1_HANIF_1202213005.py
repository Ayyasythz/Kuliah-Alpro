listMenu = []

print("===>>> PROGRAM KERANJANG BELANJAAN <<<===")
print("1. Tambah Item ke Keranjang\n2. Menghitung Jumlah Item\n3. Menampilkan Seluruh Item\n0. Exit")

l = True
while l:
    inp_pilih = int(input("Masukan Menu yang anda inginkan ?"))
    match inp_pilih :
        case 1:
            inp_tambahMenu = input("Masukan Nama Item : ")
            print(f"{inp_tambahMenu} berhasil di tambahkan")
            print()
            listMenu.append(inp_tambahMenu)
        case 2:
            print(f"Jumlah Item yang harus kaori beli sebanyak {len(listMenu)} item")
            print()
        case 3:
            print("Daftar Item yang harus dibeli")
            for x in range(0, len(listMenu)):
                print(f"{x}. {listMenu[x]}")
            print()
        case 0:
            print("Terima Kasih telah menggunakan Program Kami")
        case _:
            print(f"Tidak ada pilihan {inp_pilih} pada program kami")

