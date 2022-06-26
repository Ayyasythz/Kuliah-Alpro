def luasKubus(sisi):
    return 6 * sisi * sisi
def volumeKubus(sisi):
    return sisi*sisi*sisi

inp_sisi = float(input("Masukan Sisi : "))
l = luasKubus(inp_sisi)
v = volumeKubus(inp_sisi)
print(f"Volume Kubus : {float(round(v,2))} m^3")
print(f"Luas Permukaan Kubus : {float(round(l,2))} m^2")
