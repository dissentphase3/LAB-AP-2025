import os
from datetime import datetime
import random

def transaksiBaru(x, t): # 'x' untuk parameter list data produk; dan 't' untuk parameter total harga produk
    if len(x) == 0: # Jika 'x' kosong alias user tidak tambah produk, maka list data produk dikosongkan
        dataProduk = []
    else: # Jika user tambah produk, maka list produk sama dengan list data produk sebelumnya (rekursi)
        dataProduk = x

    print(f"{'=' * 50}")
    while True:
        try:
            namaProduk = input('Masukkan nama produk        : ')
            if len(namaProduk) == 0:
                raise Exception('\nNama tidak boleh kosong!\n')
            break
        except Exception as ex:
            print(ex)
    while True:
        try:
            hargaProduk = input('Masukkan harga produk       : ')
            if len(str(hargaProduk)) < 3 or hargaProduk[0] == '0': # Memastikan harga minimal ratusan, berupa integer, dan tidak dimulai dari nol
                raise Exception('\nHarga produk invalid!\n')
            hargaProduk = int(hargaProduk)
            break
        except ValueError:
            print('\nHarga produk invalid!\n')
        except Exception as ex:
            print(ex)
    while True:
        try:
            jumlahProduk = input('Masukkan jumlah produk      : ')
            if len(jumlahProduk) == 0 or jumlahProduk[0] == '0':
                raise ValueError
            jumlahProduk = int(jumlahProduk)
            print(f"{'=' * 50}")
            break
        except ValueError:
            print('\nJumlah produk invalid!\n')
    totalHarga = hargaProduk * jumlahProduk # Total harga setiap produk
    TOTAL = t; TOTAL += totalHarga ; RpTOTAL = f'Rp{TOTAL}'# Total harga semua produk

    dataProduk.append([namaProduk, f'Rp{hargaProduk}', jumlahProduk, f'Rp{totalHarga}']) # Menampung data produk dari user
    
    while True:
        try:
            tp = input('Tambah produk? (y / t)      : ').lower() # Menentukan apakah user ingin tambah produk
            if tp == 't':
                print(f"{'=' * 50 }\n" + 'TRANSAKSI BERHASIL'.center(50) + f"\n{'=' * 50 }")
                namaFolder = 'Invoices' # Membuat nama dir / folder
                namaTanpaSpasi = namaKasir.replace(' ','').replace('.', '') # Nama untuk ID
                tglDanWaktuIndo = datetime.now().strftime("%d/%m/%y %H:%M") # Tanggal dan waktu untuk tabel
                if len(namaTanpaSpasi) <= 3: # ID dari nama jika panjang nama kasir kurang atau sama dengan tiga karakter.
                    IDnama = namaTanpaSpasi.upper()
                else:
                    IDnama = (namaTanpaSpasi[0] + namaTanpaSpasi[len(namaTanpaSpasi) // 2] + namaTanpaSpasi[-1]).upper() # ID dari nama kasir jika panjang nama kasir lebih dari tiga karakter
                IDtglwaktu = datetime.now().strftime("%y%m%d%H%M") # ID dari tanggal dan waktu
                IDangka = str(random.randint(100, 999)) # ID dari tiga angka acak
                ID = IDnama + IDtglwaktu + IDangka # ID jika user telah melakukan transaksi
                filePath = f'{namaFolder}/{ID}.txt' # Membuat file path (tempat beserta nama file)
                if os.path.exists(namaFolder) == False: # Cek apakah dir / folder sudah ada
                    os.mkdir(namaFolder) # Membuat dir baru
                with open(filePath, 'a') as fh: # Open file
                    # Membuat tabel untuk invoices
                    fh.write('\n' + f"TOKO {namaKasir.upper()}".center(69)) 
                    fh.write(f"\n{'=' * 69}\nNama kasir         : {namaKasir}\nWaktu transaksi    : {tglDanWaktuIndo}\n{'=' * 69}")
                    fh.write('\n\n' + 'Daftar Produk'.center(69) + '\n')
                    fh.write(f"""
    {'=' * 62}
    |        Nama        |    Harga     | Jumlah |    Total      |
    {'=' * 62}""") # Format head table Daftar Produk
                    for i in range(len(dataProduk)):
                        nama = dataProduk[i][0][:15] + '...' if len(dataProduk[i][0]) > 15 else dataProduk[i][0]
                        fh.write(f"\n    | {nama:<18} |" + f" {dataProduk[i][1]:>12} |" + f" {dataProduk[i][2]:^6} " + f"| {dataProduk[i][3]:>13} |")
                    fh.write('\n' + f"{'=' * 62}".center(69))
                    fh.write('\n' + f'    |       TOTAL                                | {RpTOTAL:>13} |' + '\n')
                    fh.write(f"{'=' * 62}".center(69) + f"\n\n{'=' * 69}\n" + 'TERIMA KASIH TELAH BERBELANJA'.center(69) + f"\n{'=' * 69}")
                trxFile = 'trx_history.txt' # Membuat file untuk riwayat transaksi
                if os.path.exists(trxFile) == False: # Cek apakah file sudah ada
                    # Membuat tabel riwayat transaksi jika file belum ada
                    with open(trxFile, 'a') as tr:
                        tr.write(f"""
{'=' * 80}
|                              RIWAYAT TRANSAKSI                               |
{'=' * 80}
| {'Waktu':^20} | {'ID':^20} | {'Nominal':^30} |
{'=' * 80}""") # Format tabel riwayat transaksi jika filenya belum ada
                        tr.write(f"""
| {tglDanWaktuIndo:^20} | {ID:^20} | {RpTOTAL:>30} |
{'=' * 80}""")
                    break
                else: # Membuat tabel riwayat transaksi jika file belum ada
                    with open(trxFile, 'a') as tr:
                        tr.write(f"""
| {tglDanWaktuIndo:^20} | {ID:^20} | {RpTOTAL:>30} |
{'=' * 80}""") # Format tabel riwayat transaksi jika file sudah ada
                    break
            elif tp == 'y':
                transaksiBaru(dataProduk, TOTAL) # Jika user ingin menambahkan produk, maka terjadi rekursi dengan menggunakan ID dan list data produk sebelumnya
                break
            else: # Memastikan user hanya menginput opsi 'y' atau 't'
                raise Exception(f"{'=' * 50}\nHanya ada opsi 'y' dan 't'!\n")
        except Exception as ex:
            print(ex)

def cekTrx():
    while True:
        try:
            id = input(f"{'=' * 50}\nMasukkan ID transaksi       : ")
            filePath = f'Invoices/{id}.txt'
            if os.path.exists(filePath): # Mencari file berdasarkan ID yang dimasukkan
                print(f"{'_' * 69}")
                with open(filePath, 'r') as fh:
                    print(fh.read())
                print(f"{'_' * 69}")
                break
            else: 
                raise Warning(f"{'=' * 50}\nID invalid!\n")
        except Warning as wr:
            print(wr)

print(f"{'=' * 50}\n" + "SELAMAT DATANG".center(50) + f"\n{'=' * 50}")
while True:
    try:
        namaKasir = input("Masukkan nama kasir         : ").title()
        if (namaKasir.replace(' ','').replace('.','')).isalpha() == False: # Memastikan tidak ada karakter selain huruf, spasi, dan tanda titik
            raise Exception('\nNama harus huruf!\n')
        elif len(namaKasir) == 0: # Mematikan nama kasir tidak kosong
            raise Warning('\nNama tidak boleh kosong!\n')
        print('=' * 50)
        break
    except Warning as war:
        print(war)
    except Exception as ex:
        print(ex)
while True:
    try:
        print('Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar')
        print('=' * 50)
        opsi = input('Masukkan opsi pilihan Anda  : ')
        if opsi == '1':
            transaksiBaru('', 0)
        elif opsi == '2':
            cekTrx()
        elif opsi == '3':
            print(f"{'=' * 50}\n" + 'SAMPAI JUMPA'.center(50) + f"\n{'=' * 50}")
            break
        else:
            raise Warning(f"{'=' * 50}\nOpsi invalid!\n")
    except Warning as wr:
        print(wr)