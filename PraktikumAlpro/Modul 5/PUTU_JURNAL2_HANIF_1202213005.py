biodataDimas = {
    "nama" : "Dimas",
    "usia" : 24,
    "jurusan" : "TI",
    "ipk" : 3.48
}

print("==== Menu =====")
print("1. Menghapus Elemen\n2. Menambah Elemen\n3. Tampilkan Hasil\n0. Exit")
l = True
while l :
    inp_pilih = int(input("Pilih Opsi :"))
    match inp_pilih:
        case 1:
            hapus = input("Nama Elemen Yang ingin dihapus : ")
            if hapus not in biodataDimas:
                print(f"Tidak ada elemen dengan value {hapus}")
            else:
                biodataDimas.pop(hapus)
                print(f"{hapus} berhasil dihapus")
        case 2:
            tambah = input("Nama Elemen yang ingin ditambah : ")
            nilai = input("Masukan Nilai: ")
            biodataDimas[tambah] = nilai
            print(f"Berhasil Menambahkan Elemen {tambah} dengan nilai {nilai}")
        case 3:
            print(biodataDimas)
        case 0:
            l = False
        case _:
            print("TIdak ada Pilihan")

