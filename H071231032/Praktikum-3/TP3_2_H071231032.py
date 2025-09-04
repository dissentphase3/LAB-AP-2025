# Muhammad Qaffal Al Fifaiz | H071231032 | Tugas Pekan Ketiga
harga = int(input('Harga: '))
bayar = int(input('Bayar: '))
if harga > bayar:
    print("Uang Anda kurang.")
    quit()
kembalian = bayar - harga
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
jumlah_uang = 0

for pecahan in pecahan_uang:
    jumlah_uang = kembalian // pecahan
    kembalian %= pecahan
    pecahan = f'{pecahan:,}'.replace(',','.')
    print(f"{jumlah_uang} uang sejumlah Rp {pecahan}")