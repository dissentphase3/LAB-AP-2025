import os
import random
import datetime

if not os.path.exists("invoices"):
    os.mkdir("invoices")

transaksi = []

def hasil_id():
    now = datetime.datetime.now()
    id_transaksi = now.strftime("%y%m%d%H%M") + str(random.randint(100, 999))
    inisial = kasir[0] + kasir[len(kasir) // 2] + kasir[-1]
    return inisial.upper() + id_transaksi

def print_invoice(id_transaksi, kasir, produk):
    file_invoices = f"invoices/{id_transaksi}.txt"
    waktu_transaksi = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    
    total_harga = 0
    for _, harga, jumlah_produk in produk:
        total_harga += harga * jumlah_produk

    with open(file_invoices, "w") as f:
        panjang = "="*75
        panjang1 = "="*65
        f.write("\n")
        f.write(f"{'TOKO ' + kasir.upper():^75}\n")
        f.write("\n")
        f.write(panjang)
        f.write(f"\nNama Kasir           : {kasir}\n")
        f.write(f"Waktu Transaksi      : {waktu_transaksi}\n")
        f.write(panjang)
        f.write("\n")
        f.write(f"\n{'Daftar Produk':^75}\n")
        f.write(f"\n{panjang1:^75}\n")
        f.write("     |         Nama         |      Harga     | Jumlah |     Total    |\n")
        f.write(f"{panjang1:^75}")
        for produk1 in produk:
            nama_produk, harga, jumlah_produk = produk1
            nama_produk = nama_produk[:15] + '....' if len(nama_produk) > 15 else nama_produk
            total_produk = harga * jumlah_produk
            f.write(f"\n     | {nama_produk:<20} | Rp.{int(harga):>11} | {jumlah_produk:^6} | Rp.{int(total_produk):>9} |")
        f.write(f"\n{panjang1:^75}")
        total_harga = f'{int(total_harga)}'
        f.write(f'\n     |        TOTAL                                   | Rp.{total_harga:>9} |')
        f.write(f"\n{panjang1:^75}\n")
        f.write("\n")
        f.write(panjang)
        f.write(f"\n{'TERIMA KASIH TELAH BERBELANJA':^75}\n")
        f.write(panjang)
    return file_invoices

def cari_invoices(id_transaksi):
    file_invoices = f"invoices/{id_transaksi}.txt"
    if os.path.exists(file_invoices):
        with open(file_invoices, "r") as f:
            print(f.read())
    else:
        print(f"Invoice dengan ID {id_transaksi} tidak ditemukan.")
        
def history(id_transaksi, pembayaran):
    panjang = "="*75
    waktu = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    transaksi.append((id_transaksi, pembayaran))
    if not os.path.exists("trx_history.txt"):
        with open("trx_history.txt", "w") as f:
                f.write(panjang)
                f.write("\n|                            RIWAYAT TRANSAKSI                            |\n")
                f.write(panjang)
                f.write("\n|          Waktu          |       ID Transaksi      |  Nominal Transaksi  |\n")
                f.write(panjang)
    with open("trx_history.txt", "a") as f:
        id_transaksi1, pembayaran1 = transaksi[-1]
        pembayaran1 = f'{int(pembayaran1)}'
        f.write(f"\n| {waktu:<23} | {id_transaksi1:<23} | Rp.{pembayaran1:>16} |\n")
        f.write(panjang)
        
panjang = "="*75
print(panjang)
print(f"{'SELAMAT DATANG':^75}")
print(panjang)
kasir = input("Masukkan nama kasir       : ").title()
while True:
    print(panjang)
    print("Pilih Opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print(panjang)
    opsi = input("Masukkan opsi pilihan     : ")

    if opsi == "1":
        produk = []
        while True:
            print(panjang)
            nama_produk = input("Masukkan nama produk      : ").title()
            harga = input("Masukkan harga produk     : ")
            
            try:
                harga = float(harga)
            except ValueError:
                print("Harga harus berupa angka. Silakan masukkan harga yang valid.")
                continue  # Lanjutkan loop untuk meminta input harga yang valid
            
            jumlah_produk = int(input("Masukkan jumlah produk    : "))
            produk.append((nama_produk, harga, jumlah_produk))
            print(panjang)
            tambah = input("Tambah produk? (y/t)      : ")
            if tambah.lower() != "y":
                break
        id_transaksi = hasil_id()
        file_invoices = print_invoice(id_transaksi, kasir, produk)
        total_harga = 0
        for _, harga, jumlah_produk in produk:
            total_harga += harga * jumlah_produk
        print(panjang)
        print(f"{'TRANSAKSI BERHASIL':^75}")
        history(id_transaksi, total_harga)

    elif opsi == "2":
        print(panjang)
        id_transaksi = input("Masukkan ID transaksi     : ")
        print("_"*75)
        cari_invoices(id_transaksi)

    elif opsi == "3":
        print(panjang)
        break
    else:
        print("Silahkan pilih opsi 1-3")

print(f"{'SAMPAI JUMPA':^75}")
print(panjang)
