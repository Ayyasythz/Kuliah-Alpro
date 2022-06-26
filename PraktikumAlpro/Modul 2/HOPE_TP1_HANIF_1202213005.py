while True :
    try:
        inputNumber = int(input("Masukan Angkanya : "))
        if inputNumber % 2 == 0:
            print("Angka {} adalah Bilangan Genap".format(inputNumber))
        else:
            print("Angka {} adalah Bilangan Ganjil".format(inputNumber))
        break
    except ValueError:
        print("Masukan Angka!!")