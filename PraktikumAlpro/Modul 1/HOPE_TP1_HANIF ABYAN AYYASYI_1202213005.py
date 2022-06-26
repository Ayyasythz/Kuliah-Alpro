lups = True
while lups :
    try:
        jml_pengeluaran = int(input("Masukan Jumlah Pengeluaran Bulan ini : "))
        jml_pemasukan = int(input("Masukan Jumlah Pemasukan Bulan ini : "))
        lups = False
    except ValueError :
        print("Tolong Masukan Jumlah Nominal!!")
namaPT, alamat = "PT.XYZ", "Jl. Yos Sudarso XIII"
print("Nama     : {}\nAlamat   : {}".format(namaPT,alamat))
print("Pengeluaran :", jml_pengeluaran, "\nPemasukan : ", jml_pemasukan)
