import os.path
import datetime 
import random 

def garis_tabel(kata, len_kata_atas, arah):
    if len(kata) > len_kata_atas:
        kata = kata[:len_kata_atas-3] + '...'
    elif len(kata) < len_kata_atas:
        if arah == 'kiri':
            kata = kata.ljust(len_kata_atas)
        elif arah == 'kanan':
            kata = kata.rjust(len_kata_atas)
        elif arah == 'tengah':
            kata = kata.center(len_kata_atas)
    return kata

def buat_teks_invoice(daftar, nama_kasir, format_tanggal):
    total_harga = 0
    list_harga = []

    teks_invoice = f'''
                                TOKO {nama_kasir.upper()}                                 

================================================================================
Nama Kasir          : {nama_kasir}
Waktu Transaksi     : {format_tanggal}
================================================================================

                                Daftar Produk                                  

    ========================================================================   
    |        Nama       |     Harga      |     Jumlah     |     Total      |
    ========================================================================'''

    for i in range(len(daftar['nama'])):
        nama = daftar['nama'][i]
        harga = daftar['harga'][i]
        jumlah = daftar['jumlah'][i]
        total = harga * jumlah
        list_harga.append(total)

        teks_invoice +=f'''
    | {garis_tabel(nama, 18, 'kiri')}|{garis_tabel('Rp'+str(harga), 15, 'kanan')} |{garis_tabel(str(jumlah), 16, 'tengah')}|{garis_tabel('Rp'+str(total), 15, 'kanan')} |
    ========================================================================'''
    
    total_harga = sum(list_harga)
    
    teks_invoice +=f'''
    |     TOTAL                                           |{garis_tabel('Rp'+str(total_harga), 15, 'kanan')} |
    ========================================================================    

================================================================================
                            TERIMA KASIH TELAH BERBELANJA                          
================================================================================'''

    return teks_invoice

def simpan_invoice(teks_invoice, invoices):
    folder_path = 'Pertemuan 7/invoices'
    file_path = f'{folder_path}/{invoices}.txt'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(file_path, 'w') as invoice:
        invoice.write(teks_invoice)

list_invoice=[]
list_total_harga=[]
list_format_tanggal=[]

print('='*60)
print('SELAMAT DATANG'.center(60))
print('='*60)
nama_kasir = input('Masukkan nama kasir          : ')
list_nama_kasir = [str(nama_kasir) for nama_kasir in nama_kasir.split()]

# id_kasir = nama_kasir[0] + nama_kasir[len(nama_kasir)//2] + nama_kasir[-1]

inisial_depan = list_nama_kasir[0][0].upper()
inisial_tengah = list_nama_kasir[len(list_nama_kasir)//2][len(list_nama_kasir[len(list_nama_kasir)//2])//2].upper()
inisial_belakang = list_nama_kasir[-1][-1].upper()

waktu = datetime.datetime.now()
format_tanggal = waktu.strftime('%d/%m/%y %H:%M')
dua_digit_tahun = waktu.strftime('%y')
digit_bulan = waktu.strftime('%m')
digit_hari = waktu.strftime('%d')
empat_digit_jam = waktu.strftime('%H%M')

while True:
    print('='*60)
    print('Pilih opsi :')
    print('1. Transaksi Baru')
    print('2. Cari Transaksi')
    print('3. Keluar')
    print('='*60)
    while True:
        try:
            opsi_pilihan = int(input('Masukkan opsi pilihan        : '))
            if opsi_pilihan in (1, 2, 3):
                break
            else:
                print('Silahkan coba lagi')
        except ValueError:
            print('Silahkan coba lagi')
    print('='*60) 
    match opsi_pilihan :
        case 1 :
            daftar= {
                    'nama':[],
                    'harga':[],
                    'jumlah':[]
            }
            nilai_acak = str(random.randint(100, 999))
            while True:
                nama_produk = input('Masukkan nama produk         : ')
                harga_produk = int(input('Masukkan harga produk        : '))
                jumlah_produk = int(input('Masukkan jumlah produk       : '))

                daftar['nama'].append(nama_produk)
                daftar['harga'].append(harga_produk)
                daftar['jumlah'].append(jumlah_produk)
                print("="*60)
                tambah = input('Tambah produk? (y/t)         : ').lower()
                print("="*60)
                if tambah == 't':
                    break
            print('TRANSAKSI BERHASIL'.center(60))

            list_harga = [daftar['harga'][i] * daftar['jumlah'][i] for i in range(len(daftar['harga']))]
            total_harga = sum(list_harga)
            list_total_harga.append(total_harga)

            teks_invoice = buat_teks_invoice(daftar, nama_kasir, format_tanggal)
            
            invoices = inisial_depan + inisial_tengah + inisial_belakang + dua_digit_tahun + digit_bulan + digit_hari + empat_digit_jam + nilai_acak
            list_format_tanggal.append(format_tanggal)
            list_invoice.append(invoices)
            simpan_invoice(teks_invoice, invoices)

            teks_history= f'''
            ====================================================================================
            |                                   RIWAYAT TRANSAKSI                              |
            ====================================================================================
            |        Waktu         |       ID Transaksi         |       Nominal Transaksi      |
            ===================================================================================='''
            for i in range(len(list_invoice)):
                teks_history2=f'''
            |{garis_tabel(str(list_format_tanggal[i]),22,'tengah')}| {garis_tabel(list_invoice[i],27,'kiri')}|{garis_tabel('Rp'+str(list_total_harga[i]),30,'kanan')}|
            ===================================================================================='''
                
            # untuk write teks history
            folder_path='Pertemuan 7'
            file_path=folder_path+'/'+'trx_history'+'.txt'
            if not os.path.exists(file_path):
                with open(file_path,'w') as history:
                    history.write(teks_history)
                with open(file_path,'a') as history2:
                    history2.write(teks_history2)
            else:
                with open(file_path,'a') as history2:
                    history2.write(teks_history2)     
        case 2 :
            id_transaksi = input('Masukkan ID transaksi        : ')
            folder_path = 'Pertemuan 7/invoices'
            file_path = f'{folder_path}/{id_transaksi}.txt'
            try:
                if os.path.exists(file_path):
                    with open(file_path,'r') as transaksi:
                        isi_transaksi = transaksi.read()
                    print(isi_transaksi)
                else:
                    print('ID Transaksi Tidak Ditemukan')
            except FileNotFoundError or NameError:
                print('ID Transaksi Tidak Ditemukan')
        case 3 :
            print('SAMPAI JUMPA'.center(60))
            print('='*60)
            break