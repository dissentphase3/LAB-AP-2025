import os
import datetime
import random

# Fungsi untk membuat ID Transaksi
def IDTransaksi(namaKasir):
    Waktu = datetime.datetime.now()
    IDnama = namaKasir[0] + namaKasir[len(namaKasir) // 2] + namaKasir[-1]
    ID = f"{IDnama.upper()}{Waktu.strftime('%y%m%d%H%M')}{random.randint(100, 999)}"
    return ID

# Fungsi untuk output ke File Transaksi
def waktu():
    waktuSekarang = datetime.datetime.now()
    Waktu = f"{waktuSekarang.strftime('%d/%m/%y %H:%M')}"
    return Waktu

def tabelAtas(namaKasir, Waktu):
    file_tb.write(f"\n{f'TOKO {namaKasir.upper()}'.center(70)}\n\n")
    file_tb.write(f"{'=' * 70}\n")
    file_tb.write(f"{'Nama kasir':<20}: {namaKasir}\n")
    file_tb.write(f"{'Waktu transaksi':<20}: {Waktu}\n")
    file_tb.write(f"{'=' * 70}\n\n")
    file_tb.write(f"{'Daftar Produk'.center(70)}\n\n")
    file_tb.write(f"{60 * '=':^70}\n")
    file_tb.write(f"{5 * ' '}|{'Nama':^20}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^15}|\n")
    file_tb.write(f"{60 * '=':^70}\n")

def tabelTransaksi(namaProduk, harga, jumlah, total):
    for i in Produk: #Produk = baris produk
        namaProduk, harga, jumlah, total = i
        if len(namaProduk) >= 20:
            namaProduk = namaProduk[:15] + "..."
        file_tb.write(f"{' ' * 5}| {namaProduk:<18} | {'Rp' + str(harga):>10} |{jumlah:^8}| {'Rp' + str(total):>13} |\n")

def tabelBawah(totalProduk):
    file_tb.write(f"{60 * '=':^70}\n")
    file_tb.write(f"{' ' * 5}|{' ' * 7}{'TOTAL':<35}| {'Rp' + str(totalProduk):>13} |\n") # 7+35+13+2+3 = 60
    file_tb.write(f"{60 * '=':^70}\n\n")
    file_tb.write(f"{'=' * 70}\n")
    file_tb.write(f"{'TERIMA KASIH TELAH BERBELANJA':^70}\n")
    file_tb.write(f"{'=' * 70}\n")

# Fungsi untuk output ke File Riwayat Tansaksi
def riwayatTransaksi():
    with open('trx_history.txt', 'w') as file_ts:
        file_ts.write(f"{'=' * 70}\n")
        file_ts.write(f"|{'RIWAYAT TRANSAKSI':^68}|\n")
        file_ts.write(f"{'=' * 70}\n")
        file_ts.write(f"|{'Waktu':^18}|{'ID Transaksi':^24}|{'Nominal Transaksi':^24}|\n")
        file_ts.write(f"{'=' * 70}\n")

def isiRiwayat(Waktu, ID):
    with open('trx_history.txt', 'a') as file_isi:
        file_isi.write(f"|{Waktu:^18}|{ID:^24}| {'Rp' + str(totalProduk):>22} |\n")
        file_isi.write(f"{'=' * 70}\n")


# terminal (program utama)
print("=" * 60)
print("SELAMAT DATANG".center(60))
print("=" * 60)
namaKasir = input('Masukkan nama kasir \t: ').title()
print("=" * 60)

while True:
    print("1. Transaksi Baru\n2. Cari Transaksi\n3. Keluar")
    print("=" * 60)
    opsi = int(input("Masukkan opsi pilihan \t: "))
    print("=" * 60)

    match opsi:
        case 1:
            Produk = []
            totalProduk = 0 #total
            while True:
                namaProduk = str(input("Masukkan nama produk \t: "))
                hargaProduk = input("Masukkan harga produk \t: ")   
                while not hargaProduk.isdigit():
                    print("Harga produk harus berupa angka. Silakan coba lagi.")
                    hargaProduk = input("Masukkan harga produk \t: " )
                jumlahProduk = input("Masukkan jumlah produk \t: ")
                while not jumlahProduk.isdigit():
                    print("Jumlah produk harus berupa angka. Silakan coba lagi.")
                    jumlahProduk = input("Masukkan jumlah produk \t: " )
                harga = int(hargaProduk)
                jumlah = int(jumlahProduk)
                total = harga * jumlah
                print("=" * 60)

                Produk.append((namaProduk, harga, jumlah, total))
                totalProduk += total

                opsiTambah = input('Tambah Produk? (y/t) \t: ').lower()
                while opsiTambah not in ('y', 't'):
                    print("Anda hanya dapat menginput 'y' atau 't'. Silahkan coba lagi.")
                    opsiTambah = input("Tambah Produk? (y/t) \t: ").lower()
                if opsiTambah == "y":
                    print("=" * 60)
                    continue
                elif opsiTambah == "t":
                    print("=" * 60)
                    print("TRANSAKSI BERHASIL".center(60))
                    print("=" * 60)

                    # Membuat File Transaksi
                    ID = IDTransaksi(namaKasir)
                    nama_File = f'{ID}.txt'
                    nama_Folder = "invoices"
                    file_Path = os.path.join(nama_Folder, nama_File)

                    Waktu = waktu()
                    
                    # Membuat Folder jika Foldernya belum ada
                    if not os.path.exists(nama_Folder):
                        os.mkdir(nama_Folder)
                    
                    file_tb = open(file_Path, "w")
                    
                    tabelAtas(namaKasir, Waktu)
                    tabelTransaksi(namaProduk, harga, jumlah, total)
                    tabelBawah(totalProduk)

                    file_tb.close()

                    # Membuat File Riwayat jika File belum ada
                    if not os.path.exists("trx_history.txt"):
                        riwayatTransaksi()
                
                    isiRiwayat(Waktu, ID)

                    break
                else:
                    print("=" * 60)
                    print("Invalid pilihan")
                    break

        case 2:
            Cari = input("Masukkan ID transaksi \t: ")
            Nama_Folder = "invoices"
            Cari_Path = os.path.join(Nama_Folder, f"{Cari}.txt")

            if os.path.exists(Cari_Path):
                with open(Cari_Path, "r") as file:
                    print('_' * 70)
                    print(f"\n{file.read()}")
                    print('_' * 70)   
            else:
                print(f"File dengan ID {Cari} tidak ditemukan.")
                print("=" * 60)
        
        case 3:
            print("SAMPAI JUMPA".center(60))
            print("=" * 60)
            break

        case _:
            print("Invalid Opsi!".center(60))
            print("=" * 60)
            continue