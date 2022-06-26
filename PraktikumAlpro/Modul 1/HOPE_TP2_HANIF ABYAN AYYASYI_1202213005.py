lups =  True
namaPT= "PT. Pejuang Muda"
print("=== Hasil Penjualan {} ===".format(namaPT))
while lups :
    try:
        pj_besiHollow = int(input("Masukan hasil penjualan besi Hollow bulan ini = "))
        pj_besiSiku = int(input("Masukan hasil penjualan besi Siku bulan ini = "))
        pj_besiPlat = int(input("Masukan hasil penjualan besi Plat bulan ini = "))
        pj_pipaBesi = int(input("Masukan hasil penjualan Pipa besi bulan ini = "))
        lups = False
    except ValueError :
        print("Masukan Nominal!!!")
avg_pjl = (pj_besiHollow + pj_besiSiku + pj_besiPlat + pj_pipaBesi) / 4
print("Hasil Rate-Rata Penjualan Bulan ini Rp. {}".format(avg_pjl))

