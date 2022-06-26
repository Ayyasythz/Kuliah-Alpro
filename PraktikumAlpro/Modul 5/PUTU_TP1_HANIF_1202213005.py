def printMenu():
    print("===>>> PROGRAM MANAJEMEN DATA NILAI UJIAN <<<===")
    print(
        "1. Tambah Nilai\n2. Mengurutkan Nilai\n3. Rata-rata Nilai\n4. Menghapus Nilai\n5. Menampilkan Seluruh Nilai "
        "\n0. Exit")


listNilai = []

l = True
while l:
    printMenu()
    print()
    pilih = int(input("Masukan menu yang Anda inginkan : "))
    match pilih:
        case 1:
            k = True
            while k:
                inp_nilai = int(input("Masukan Nilai :"))
                if inp_nilai not in range(0, 101):
                    k = True
                else:
                    listNilai.append(inp_nilai)
                    k = False

        case 2:
            a = sorted(listNilai)
            print("Data Nilai Ujian :")
            for x in range(0, len(a)):
                print(f"{x + 1}. {a[x]}")

        case 3:
            sum, mean, coun = 0, 0, 0
            for x in range(0, len(listNilai)):
                sum += listNilai[x]
                coun = x + 1
            mean = sum / coun
            print(f"Rata-rata nilai ujian adalah {mean}")

        case 4:
            inp_dataHapus = int(input("Masukan data yang akan dihapus :"))
            ada = listNilai.count(inp_dataHapus)
            if ada > 0:
                listNilai.remove(inp_dataHapus)
                print(f"Data Nilai Ujian sebesar {inp_dataHapus} telah dihapus")
            else:
                print("Nilai Tidak ada")

        case 5:
            for x in range(0, len(listNilai)):
                print(f"{x + 1}. {listNilai[x]}")

        case 0:
            print("Terima Kasih Telah Menggunakan Program Kami")
            l = False
        case _:
            print("Menu yang Anda Masukan tidak tersedia, silahkan pilih menu lain")
