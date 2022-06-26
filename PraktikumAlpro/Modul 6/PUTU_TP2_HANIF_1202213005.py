print("|| Program Tantangan Mr. D ||")
inp_nama = input("Masukan Nama: ")
inp_nim = input("Masukan NIM : ")
inp_kelas = input("Masukan Kelas : ")
inp_status = input("Masukan Status : ")
namaFile = "output.txt"
with open(namaFile,'w+') as x:
    x.write(f"Halo Perkenalkan namaku {inp_nama}\ndengan NIM {inp_nim} saya ada di kelas {inp_kelas}\nStatus "
            f"hubunganku saat ini {inp_status}, hehehe <3")
    x.close()


