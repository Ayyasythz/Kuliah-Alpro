inp_kata = input("Masukan Kata: ")
tupleKata = ()
for x in range(0, len(inp_kata)):
    a = inp_kata[x]
    b = (a,)
    tupleKata += b

print(f"Kata dalam bentuk tuple: {tupleKata}")

print("==== Menu Tuple =====")
print("1. Jumlah huruf\n2. Membalik Urutan\n3. Menghapus Huruf Pertama\n 0. Exit")


l = True
while l :
    inp_pilih = int(input("Pilih Opsi : "))
    match inp_pilih:
        case 1:
            print(f"Jumlah Huruf : {len(tupleKata)}")
        case 2:
            reverse = tupleKata[::-1]
            print(f"Hasil membalikan urutan: {reverse}")
        case 3:
            hilang_first = tupleKata[1:]
            print(f"Hasil menghapus huruf pertama: {hilang_first}")
        case 0:
            l = False
        case _:
            print(f"Tidak ada pilihan {inp_pilih} di program ini")
