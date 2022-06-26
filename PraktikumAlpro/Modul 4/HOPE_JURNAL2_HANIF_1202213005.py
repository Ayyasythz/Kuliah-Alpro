class Bioskop:
    def __init__(self, nama_penyewa, jml_penonton, genre):
        self.nama_penyewa = nama_penyewa
        self.jml_penonton = jml_penonton
        self.genre = genre

    def valiasiJMlPenonton(self):
        if self.jml_penonton in range(1, 51):
            print(f"{self.nama_penyewa} menyewa studio type A")
        elif self.jml_penonton in range(51, 101):
            print(f"{self.nama_penyewa} menyewa studio type B")
        elif self.jml_penonton in range(101, 151):
            print(f"{self.nama_penyewa} menyewa studio type C")
        elif self.jml_penonton > 150:
            print(f"Bioskop Tidak Bisa Menampung")
        else:
            print("Yang bener dong bangh")


if __name__ == '__main__':
    inp_nama = input("Nama            :")
    inp_jml_penonton = int(input("Jumlah Penonton : "))
    inp_genre = input("Genre           : ")
    object1 = Bioskop(inp_nama, inp_jml_penonton, inp_genre)
    print()
    object1.valiasiJMlPenonton()
