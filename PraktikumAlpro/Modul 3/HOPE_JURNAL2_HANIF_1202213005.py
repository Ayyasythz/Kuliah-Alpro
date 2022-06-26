print("=== Program absen infinity ===")
print("Masukan nama pendek untuk mengabsen !")
print("Ketik stop untuk menghentikan perulangan")
x = 0
lups = True
while lups :
    nama = input("Masukan nama kamu : ")
    x += 1
    if nama.lower() != "stop" :
        if x % 3 == 0 and x % 5 == 0:
            print("HEYAHO AW")
        elif x % 3 == 0:
            print("HEYA")
        elif x % 5 == 0:
            print("HEYO")
        else:
            print("HEHE")
    else:
        print(f"Jumlah Hadir {x-1}")
        break
