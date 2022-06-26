def printMenu():
    print("=== PENDATAAN REMAJA MASJID ===")
    print("1. Tambah Remaja\n2. Cek Data\n3. Hapus Remaja\n4. Exit")


setRemaja = set()

l = True
while l:
    printMenu()
    inp_pilihMenu = int(input("Silahkan Pilih Menu : "))
    match inp_pilihMenu:
        case 1:
            inp_namaRemaja = str(input("Masukan Nama Remaja : "))
            setRemaja.add(inp_namaRemaja)
        case 2:
            print(setRemaja)
            output = ",".join(setRemaja)
            total = 0
            for x in range(0,len(setRemaja)):
                total = x+1

            print(f"Data Seluruh Remaja : {output}")
            print(f"Total Remaja : {total}")
        case 3:
            inp_hapus = str(input("Nama Remaja yang ingin dihapus : "))
            setRemaja.discard(inp_hapus)
        case 4:
            l = False
        case _:
            print("Menu yang Anda Masukan tidak tersedia, silahkan pilih menu lain")

