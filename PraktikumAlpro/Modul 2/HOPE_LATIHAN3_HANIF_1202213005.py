menu = ["Pintu dan Jendela", "CCTV", "Alarm"]
print("====MENU====")
for x in range(0,len(menu)):
    print(f"{x+1}. {menu[x]}")

pilihanMenu = int(input("Masukan Pilihan anda : "))
match pilihanMenu:
    case 1:
        print("1. Kunci \n2. Buka Kunci")
        pilihanBuka = int(input("Masukan Pilihan Anda: "))
        match pilihanBuka:
            case 1 :
                print(f"{menu[0]} telah Terkunci")
            case 2:
                print(f"{menu[0]} telah Terbuka")
            case _:
                print("Saya tidak mengerti inputanya")
    case 2:
        print("1. Nyalakan \n2. Matikan")
        pilihanBuka = int(input("Masukan Pilihan Anda: "))
        match pilihanBuka:
            case 1:
                print(f"{menu[1]} dinyalakan")
            case 2:
                print(f"{menu[1]} dimatikan")
            case _:
                print("Saya tidak mengerti inputanya")
    case 3:
        print("1. Nyalakan \n2. Matikan")
        pilihanBuka = int(input("Masukan Pilihan Anda: "))
        match pilihanBuka:
            case 1:
                print(f"{menu[2]} dinyalakan")
            case 2:
                print(f"{menu[2]} dimatikan")
            case _:
                print("Saya tidak mengerti inputanya")
    case _:
        print("Saya tidak mengerti inputanya")