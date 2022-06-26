def absen():
    l = True
    while l:
        print("input 'stop' untuk berhenti")
        nama = input("Masukan nama partisipan: ")
        if nama.lower() != "stop":
            listAbsen.append(nama)
        else:
            l = False


print("================= Peserta Seminar =================")
listAbsen = []
absen()
print("Partisipan yang hadir ada : ", ', '.join(listAbsen))
