print("=== Hasil Penjualan PT.Pejuan Muda ===")
hsl_penjualan_besi_hollow = int(input("Masukan hasil penjualan besi Hollow bulan ini = "))
hsl_penjualan_besi_siku = int(input("Masukan hasil penjualan besi Siku bulan ini = "))
hsl_penjualan_besi_plat = int(input("Masukan hasil penjualan besi Plat bulan ini = "))
hsl_penjualan_pipa_besi = int(input("Masukan hasil penjualan Pipa besi bulan ini = "))
rata_rata_penjualan = (hsl_penjualan_pipa_besi +hsl_penjualan_besi_plat+hsl_penjualan_besi_siku+hsl_penjualan_besi_hollow) / 4
print("Hasil Rata-Rata Penjualan Bulan Ini Rp.", rata_rata_penjualan)