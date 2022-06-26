print("SELAMAT DATANG DI PROGRAM MENENTUKAN INDEX KELULUSAN")

try:
    inp_nilai = int(input("Masukan Nilai Anda! : "))
    indeks = ""
    if inp_nilai >= 80:
        indeks = "A"
        print(f"Indeks Kamu adalah {indeks}")
    elif 60 < inp_nilai < 79:
        indeks = "B"
        print(f"Indeks Kamu adalah {indeks}")
    elif 40 < inp_nilai < 59:
        indeks = "C"
        print(f"Indeks Kamu adalah {indeks}")
    elif 20 < inp_nilai < 40:
        indeks = "D"
        print(f"Indeks Kamu adalah {indeks}")

except ValueError:
    print("Program Tidak Menerima String!!")

finally:
    print("Program Selesai")