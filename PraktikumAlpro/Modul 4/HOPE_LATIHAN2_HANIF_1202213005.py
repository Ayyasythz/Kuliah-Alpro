def kelompokUsia(usia):
    if usia in range(20, 35):
        return "Pekerja Awal"
    elif usia in range(35, 45):
        return "Paruh Baya"
    elif usia in range(45, 55):
        return "Pra Pensiun"
    elif usia > 54:
        return "Pensium"
    else:
        return "Masih dibawah umur bekerja"


inp_nama = input("Masukan Nama :".ljust(15))
inp_usia = int(input("Masukan Usia :".ljust(15)))
inp_asalPlanet = input("Masukan Asal Pelanet :".ljust(15))
categori_usia = kelompokUsia(inp_usia)

print("=== KARTU NAMA ===")
print("Nama".ljust(15),f": {inp_nama}")
print("Usia".ljust(15),f": {inp_usia}")
print("Kelompok Usia".ljust(15),f": {categori_usia}")
print("Asal Planet".ljust(15),f": {inp_asalPlanet}")
