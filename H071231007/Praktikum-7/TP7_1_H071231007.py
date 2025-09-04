import os
import datetime
import random

def GGG():
    print('='*70)

def createHistory():
    """fungsi untuk membuat file history dan juga tabelnya"""
    with open("trx_history.txt", 'w') as file:
        file.write(f"{'='*70}\n")
        file.write(f"|{'RIWAYAT TRANSAKSI':^68}|\n")
        file.write(f"{'='*70}\n")
        file.write(f"|{'Waktu':^18}|{'ID Transaksi':^24}|{'Nominal Transaksi':^24}|\n")
        file.write(f"{'='*70}\n")

def addHistory(waktu, id, nominal):
    """fungsi untuk menambah isi dari history transaksi"""
    with open("trx_history.txt",'a') as file:
        file.write(f"|{waktu:^18}|{id:<24}|{'Rp' + str(nominal):^24}|\n")
        file.write(f"{'-'*70}\n")

def struk():
    """fungsi untuk membuat seluruh isi struk atau invoices"""
    global kasir, WAKTU, tampung, total_belanja, file_path
    with open(file_path, "w") as data:
        data.write(f"{'TOKO CHINA':^70}\n\n")
        data.write(f"{'='*70}\n")
        data.write(f"Nama kasir \t\t: {kasir}\n")
        data.write(f"Waktu transaksi \t: {WAKTU}\n")
        data.write(f"{'='*70}\n\n")
        data.write(f"{'Daftar Produk':^70}\n\n")
        data.write(f"{60*'=':^70}\n")
        data.write(f"{5*' '}|{'Nama':^20}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^15}|\n")
        data.write(f"{60*'=':^70}\n")
        for item in daftar_item:
            if len(item["nama"]) > 20:
                item["nama"] = item["nama"][:17] + "..."
            data.write(f"{5*' '}|{item['nama']:<20}|{'Rp' + str(item['harga']):>12}|{item['jumlah']:^8}|{'Rp' + str(item['total barang']):>15}|\n")
        data.write(f"{60*'=':^70}\n")
        data.write(f"{' '*5}|{'TOTAL':^42}|{'Rp' + str(total_belanja):>15}|\n")
        data.write(f"{60*'=':^70}\n\n")
        data.write(f"{'='*70}\n")
        data.write(f"{'TERIMA KASIH TELAH BERBELANJA':^70}\n")
        data.write(f"{'='*70}\n")

def id(kasir):
    """
    fungsi untuk membuat id file berdasarkan format yang telah ditentukan
    formatnya yaitu inisial,tahun,bulan,hari,jam,menit,detik dan angka random(100-999)
    """
    inisial = ""
    x = kasir [0].upper()  + kasir [len(kasir)//2].upper() + kasir[-1].upper()
    waktu = datetime.datetime.now()
    file_name = x+ waktu.strftime("%y%m%d%H%M") + str(random.randint(100,999))
    return file_name

folder_path = "Invoices"
daftar_item = []

GGG()
print('SELAMAT DATANG'.center(70))
GGG()
kasir = input("Masukkan nama Kasir\t: ").title()

while True:
    GGG()
    print('Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar')
    GGG()
    opsi = int(input("Masukkkan opsi pilihan\t: "))
    GGG()
    match opsi:
        case 1:
            ID = id(kasir)
            file_name = ID + ".txt"
            file_path = os.path.join(folder_path, file_name)
            
            waktu = datetime.datetime.now()
            WAKTU = waktu.strftime("%y/%m/%d %H:%M")
            total_belanja = 0      

            while True:
                nama = input("Masukkan nama produk\t: ")
                harga = int(input("Masukkan harga produk\t: "))
                jumlah = int(input("Masukkan jumlah produk\t: "))
                total_barang = harga*jumlah
                total_belanja += total_barang
                GGG()

                # setiap item yang dibeli akan menjadi dictionary dan ditampung dalam list
                item = {
                    "nama" : nama,
                    "harga" : harga,
                    "jumlah" : jumlah,
                    "total barang" : total_barang,
                }
                daftar_item.append(item)
                
                isTambah = input("Tambah produk? (y/t)\t: ")
                if isTambah == 't':
                    # jika folder invoices tidak ada maka dibuat dulu
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)

                    #jika file history belum ada maka dibuat dulu
                    if not os.path.exists("trx_history.txt"):
                        createHistory()
                    #pembuatan struk
                    struk()
                    #data yang ditampung dihapus
                    daftar_item.clear()
                    GGG()
                    print(f"{'TRANSAKSI BERHASIL':^70}")
                    break
                GGG()

            # riwayat transaksi
            addHistory(WAKTU, ID, total_belanja)

        case 2:
            cari = input("Masukkan ID file transaksi : ")
            cari_path = folder_path + "/" + cari + ".txt"
            if os.path.exists(cari_path):
                with open(cari_path, "r") as file:
                    GGG()
                    print(f"\n\n{file.read()}")
            else:
                print(f"File dengan ID {cari} tidak ditemukan")

        case 3:
            print(f"SEE YOU {kasir.upper()}".center(70))
            GGG()
            break
        
        case _:
            print("INPUT TIDAK VALID".center(70))

