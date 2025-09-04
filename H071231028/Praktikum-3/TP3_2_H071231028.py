price_b = int(input("Harga barang: "))
money_d = int(input("Jumlah uang dibayarkan: "))
kembalian = money_d - price_b
pecahan_money = [100000, 50000, 20000, 10000, 5000, 2000, 1000,]

if kembalian < 0:
    print("Uang Anda tidak cukup")
else:
    for pecahan in pecahan_money:
        jumlah = kembalian // pecahan
        print(f'{jumlah} uang sejumlah Rp.{pecahan}')
        kembalian -= jumlah * pecahan
