hargabarang = int(input("Masukkan Harga Barang : ")) 
uang = int(input("Masukkan Berapa uang anda : ")) 
kembalian = uang - hargabarang 
if kembalian < 0: 
    print("Uang anda kurang!")
else: 
    pecahan = (100000, 50000, 20000, 10000, 5000, 2000, 1000) 
    for i in range(7): 
        jumlah = kembalian // (pecahan[i]) 
        kembalian = kembalian - jumlah * (pecahan[i]) 
        print(f"{jumlah} Jumlah uang bernilai Rp.{pecahan[i]}") 
