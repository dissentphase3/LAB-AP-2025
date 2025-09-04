hargaBarang = int(input("Masukkan Harga Barang : "))
uang = int(input("Masukkan Uang Yang Dibayarkan : "))
kembalian = uang - hargaBarang
if kembalian < 0:
    print("Uang anda kurang!")
else:
    pecahan = (100000, 50000, 20000, 10000, 5000, 2000, 1000)
    for i in range(0, 7):
        jumlahUang = kembalian // (pecahan[i])
        kembalian = kembalian % (pecahan[i])
        print(f"{jumlahUang} uang sejumlah Rp.{pecahan[i]}")