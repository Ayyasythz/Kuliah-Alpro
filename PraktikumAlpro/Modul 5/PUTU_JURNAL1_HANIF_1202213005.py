listUCUP = []
sum = 0

print("---- Celengan Pintar -----")
l = True
while l:
    inp_thr = int(input("Masukan uang THR Ucup (0 untuk berhenti) :"))
    if inp_thr == 0:
        l = False
    else:
        listUCUP.append(inp_thr)


mins = listUCUP[0]

for x in range(0, len(listUCUP)):
    sum += listUCUP[x]
    if listUCUP[x] < mins:
        mins = listUCUP[x]

print(f"Nominal uang THR terkecil Ucup adalah : {mins}")
print(f"Jumlah uang THR Ucup adalah : {sum}")









