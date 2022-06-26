namaFile = "Tambahin.txt"

inp_nama = input("Masukan Nama : ")
inp_kelas = input("Masukan Kelas : ")
inp_NIM = input("Masukan NIM : ")
inp_motto = input("Masukan Motto : ")

with open(namaFile,'a') as x:
    x.write(f"=============================\nNama : {inp_nama}\nKelas : {inp_kelas}\nNIM: {inp_NIM}\nMotto : {inp_motto}")
    x.close()
