bilangan_1 = int(input("Masukan bilangan 1 : "))
operasi = input("Masukan operasinya (* / ) : ")
bilangan_2 = int(input("Masukan bilangan 2 : "))

match operasi:
    case "*":
        print(f"Hasil Operasi {bilangan_1} {operasi} {bilangan_2} = {bilangan_1 * bilangan_2}")
    case "/":
        print(f"Hasil Operasi {bilangan_1} {operasi} {bilangan_2} = {bilangan_1 / bilangan_2}")

