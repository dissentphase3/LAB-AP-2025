import os
import datetime
import random

def Input_K():
    while True:
        try:
            Kasir = input("Masukkan nama kasir: ").title()
            if (Kasir.replace(' ', '').replace('.', '')).isalpha() == False:
                raise Exception('\nNama harus terdiri dari huruf!\n')
            elif len(Kasir) == 0:
                raise Exception('\nNama kasir tidak boleh kosong!\n')
            return Kasir
        except Exception as s:
            print(s)

def Transaksi_B(ID_P, Produk, T_H, Kasir, TOTAL):
    while True:
        try:
            print(f"{'=' * 50}")
            N_Produk = input('Masukkan nama produk        : ').capitalize()
            break
        except ValueError:
            print("Nama invalid.")
    while True:
        try:
            H_Produk = input('Masukkan harga produk       : ')
            if len(str(H_Produk)) < 3 or H_Produk[0] == '0':
                raise Exception('\nHarga produk invalid!\n')
            H_Produk = int(H_Produk)
            break
        except ValueError:
            print('\nHarga produk invalid!\n')
        except Exception as s:
            print(s)

    while True:
        try:
            J_Produk = input('Masukkan jumlah produk      : ')
            if J_Produk[0] == '0':
                raise ValueError
            J_Produk = int(J_Produk)
            print(f"{'=' * 50}")
            break
        except ValueError:
            print('\nJumlah produk invalid!\n')

    T_Harga = int(H_Produk * J_Produk)
    TOTAL += T_Harga
    RpTOTAL = f'Rp.{TOTAL}'

    Nospace = Kasir.replace(' ','')
    Waktu = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        
    if len(Nospace) <= 3:
        IDnama = Nospace.upper()
    else:
        IDnama = (Nospace[0] + Nospace[len(Nospace) // 2] + Nospace[-1]).upper()
    
    T_Waktu = datetime.datetime.now().strftime("%y%m%d%H%M")
    Angka = str(random.randint(100, 999))
        
    if len(ID_P) == 1:
        ID = IDnama + T_Waktu + Angka
    else:
        ID = ID_P

    Produk.append([N_Produk, f'Rp.{H_Produk}', J_Produk, f'Rp.{T_Harga}'])
        
    while True:
        try:
            YandN = input('Tambah produk? (y/t)      : ').lower()
            if YandN == 't':
                print(f"{'=' * 50 }\n" + 'TRANSAKSI BERHASIL'.center(50) + f"\n{'=' * 50}")
                N_Folder = 'Invoices'
                filePath = f'{N_Folder}/{ID}.txt'
                if os.path.exists(N_Folder) == False:
                    os.mkdir(N_Folder)

                with open(filePath, 'a') as File:
                    File.write('\n' + f"TOKO {Kasir.upper()}".center(79))
                    File.write(f"\n{'=' * 79}\nNama kasir         : {Kasir}\nWaktu transaksi    : {Waktu}\n{'=' * 79}")
                    File.write('\n\n' + 'Daftar Produk'.center(79) + '\n')
                    File.write(f"""
    {'=' * 72}
    |        Nama       |     Harga      |     Jumlah     |     Total      |
    {'=' * 72}""")
                    for i in range(len(Produk)):
                        nama = Produk[i][0][:15] + '...' if len(Produk[i][0]) > 15 else Produk[i][0][:15]
                        File.write(f"\n    | {nama:<17} |" + f" {Produk[i][1]:>14} |" + f" {Produk[i][2]:^14} " + f"| {Produk[i][3]:>14} |")
                    File.write('\n' + f"{'=' * 72}".center(79))
                    File.write('\n' + f'    |       TOTAL                                         | {RpTOTAL:>14} |' + '\n')
                    File.write(f"{'=' * 72}".center(79) + f"\n\n{'=' * 79}\n" + 'TERIMA KASIH TELAH BERBELANJA'.center(79) + f"\n{'=' * 79}")

                trxFile = 'trx_history.txt'

                if os.path.exists(trxFile) == False:
                    with open(trxFile, 'a') as tr:
                        tr.write(f"""
{'=' * 80}
|                              RIWAYAT TRANSAKSI                               |
{'=' * 80}
| {'Waktu':^20} | {'ID':^20} | {'Nominal':^30} |
{'=' * 80}""")
                        tr.write(f"""
| {Waktu:^20} | {ID:^20} | {RpTOTAL:>30} |
{'=' * 80}""")
                    break
                else:
                    with open(trxFile, 'a') as tr:
                        tr.write(f"""
| {Waktu:^20} | {ID:^20} | {RpTOTAL:>30} |
{'=' * 80}""")
                    break
            elif YandN == 'y':
                TOTAL = Transaksi_B(ID, Produk, T_H, Kasir, TOTAL)
                break
            else:
                raise Exception(f"{'=' * 50}\nHanya ada opsi 'y' dan 't'!\n")
        except Exception as s:
            print(s)

def cekTrx():
    while True:
        try:
            id = input(f"{'=' * 50}\nMasukkan ID transaksi       : ")
            filePath = f'Invoices/{id}.txt'
            if os.path.exists(filePath):
                print(f"{'_' * 79}")
                with open(filePath, 'r') as File:
                    print(File.read())
                print(f"{'_' * 79}")
                break
            else:
                raise Warning(f"{'=' * 50}\nID invalid!\n")
        except Warning as S:
            print(S)

print(f"{'=' * 50}\n" + "SELAMAT DATANG".center(50) + f"\n{'=' * 50}")

Kasir = Input_K()

print("=" * 50)
while True:
    try:
        print('Pilih opsi:')
        print('1. Transaksi baru')
        print('2. Cari transaksi')
        print('3. Keluar')
        print('=' * 50)
        opsi = input('Masukkan opsi pilihan Anda  : ')
        if opsi == '1':
            Transaksi_B('1', [], 0, Kasir, 0)
        elif opsi == '2':
            cekTrx()
        elif opsi == '3':
            print(f"{'=' * 50}\n" + 'BYE'.center(50) + f"\n{'=' * 50}")
            break
        else:
            raise Warning(f"{'=' * 50}\nOpsi invalid!\n")
    except Warning as S:
        print(S)