print("1. Bandung \n2. Jakarta \n3. Medan")
inputKota = str(input("Masukan Nama Kota : ")).lower()

match inputKota:
    case "bandung":
        print("Destinasi Wisata di Bandung diantaranya ada Farm House, Gunung Puntang, Jalan Asia Afrika")
    case "jakarta":
        print("Destinasi Wisata di Jakarta diantaranya ada TMII, Ancol, Kebon Jeruk")
    case "medan":
        print("Destinasi Wisata di Medan diantaranya ada Istana Maimun Medan, Museum Tjong A Fie, Masjid Raya Al-Mahsun")
    case _:
        print("TIdak Ada di Dalam list kami")

