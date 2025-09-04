harga = int(input())
uang = int(input())

kembalian = uang - harga
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if kembalian < 0 :
    print("Uang tidak cukup")
    
else :
    for pecahan in pecahan_uang:
        jumlah = kembalian // pecahan
        kembalian %= pecahan
        print(f"{jumlah} uang sejumlah Rp.{pecahan}")
