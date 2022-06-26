katas = ""
loop = True
while loop:
    kata = str(input("Masukan sebuah kata : "))
    if kata.lower() != "stop":
        katas += " " + kata
        continue
    else:
        print(f"Hasil Kalimat: {katas}")
        break

