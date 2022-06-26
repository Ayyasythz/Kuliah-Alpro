print("===Input Nilai Keamanan Sistem Informasi===")
sum = 0
for x in range(0,3):
    nilai = int(input("Masukan nilai minggu ke-{} : ".format(x+1)))
    sum += nilai
nama = str(input("Nama : "))
nim = str(input("NIM : "))
kelas = str(input("Kelas : "))
mean = sum / 3

print("Nilai Rata Rata Keamanan Sistem Informasi : {}".format(mean))