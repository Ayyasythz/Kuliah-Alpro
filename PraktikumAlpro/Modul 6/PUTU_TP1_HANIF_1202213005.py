print("===[ Aplikasi E-SHOES ]===")
inputMerek = input("Masukan Sepatu : ")
l = True
while l :
    try:
        inputUkuran = int(input("Masukan Ukuran Sepatu : "))
    except ValueError:
        print("Input Salah! Masukan dengan Integer")
    else:
        l = False

print("Terima Kasih sudah menggunakan Toko Sepatu Online!")
