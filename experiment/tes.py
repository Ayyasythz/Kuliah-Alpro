import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

transactions = np.array([
    [0, 282000, 3, 0],
    [1, 125000, 1, 0],
    [2, 374000, 2, 0],
    [3, 156000, 1, 0],
    [4, 174000, 2, 0],
    [5, 131000, 1, 0],
    [6, 178000, 3, 0],
    [7, 119000, 1, 0],
    [8, 117000, 1, 0],
    [9, 286000, 2, 0],
    [10, 335000, 2, 0],
    [11, 295000, 3, 0],
    [12, 194000, 3, 0],
    [13, 278000, 1, 0],
    [14, 316000, 2, 0],
    [15, 120000, 1, 0],
    [16, 171000, 2, 0],
    [17, 358000, 1, 0],
    [18, 183000, 1, 0],
    [19, 78000, 1, 0]
])



for t in range(0,len(transactions)):
    a = transactions[t][1] / 100000
    if transactions[t][2] >= 3:
        c = int(a) * 2
    else:
        c = int(a)
    transactions[t][3] = c
print("Poin")
print(transactions)
print()

a = transactions[transactions[:,1].argsort()]
print("Sort")
print(a)

mean = transactions[:,1].mean()
print(mean)

med = np.median(transactions, axis=0)
print(med[1])

deviasi = np.std(transactions,axis=0)
print(deviasi[1])
tot_keuntungan = 0
list_keuntungan = []
for x in range(0,len(transactions)):
    keuntungan = transactions[x][1] / 2
    list_keuntungan.append(keuntungan)
    print(f"Keuntungan {x} : {keuntungan}")
    tot_keuntungan += keuntungan
print(f"Total Keuntungan = {tot_keuntungan}")


mean2 = transactions[:,2].mean()
print(f"Rata Rata Jumlah Produk per Transaksi : {mean2}")

ds = 0
for z in range(0, len(transactions)):
    k = transactions[z][3] * 5000
    ds += k


print(tot_keuntungan-ds)

labels = []
listHarga = []
for h in range(0,len(transactions)):
    labels.append(transactions[h][0])
    listHarga.append(transactions[h][1])


print(labels)


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,list_keuntungan , width, label='Keuntungan')
rects2 = ax.bar(x + width/2, listHarga, width, label='Harga')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

























