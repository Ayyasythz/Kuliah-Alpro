inp_jumlah = int(input("Masukan Jumlah : "))

setA,setB = set(),set()
print("=== SET A ===")
for a in range(0,inp_jumlah):
    inp_inputSet = int(input("Masukan set 1 : "))
    setA.add(inp_inputSet)

print()
print("=== SET B ===")
for b in range(0,inp_jumlah):
    inp_inputSet = int(input("Masukan set 2 : "))
    setB.add(inp_inputSet)

tuple_awalSet = (setA,setB)

irisan = setA&setB
print()
if len(irisan) > 0:
    print(f"Set Intersection : {irisan}")
else:
    print("Tida Ada yang diiiris")
gabungan = setA|setB
print(f"Set Union : {gabungan}")

