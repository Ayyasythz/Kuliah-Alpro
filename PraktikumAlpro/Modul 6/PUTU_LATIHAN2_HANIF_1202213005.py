listAngka = [1,2,54,3,12,5,123,125,2,12]

try:
    inp_index = int(input("Ingin Index angka berapa nih DECK ? "))
    print(f"Index ke- {inp_index} adalah {listAngka[inp_index]}")
except IndexError:
    print(f"Index {inp_index} gak ada deck ")