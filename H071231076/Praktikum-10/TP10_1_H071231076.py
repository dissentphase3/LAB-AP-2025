import os.path
import re

class User:
    def __init__(self):
        self.hasil_nama = ''
        self.hasil_email = ''
        self.hasil_password = ''

    def cek_email(self, email):
        pattern = r'^[a-z.]+(\d{2,})?@student\.unhas\.ac\.id$'
        return re.match(pattern, email)

    def detail_user(self):
        if self.hasil_email:
            print('Data anda adalah')
            print(f'Nama : {self.hasil_nama}')
            print(f'Email : {self.hasil_email}')
            print(f'Password : {self.hasil_password}')
        else:
            print('Data saat ini Kosong')

    def ubah_nama(self):
        if self.hasil_nama:
            nama_baru = input('Silahkan Input Nama Baru : ')
            self.hasil_nama = nama_baru
        else:
            print('Data saat ini Kosong')

    def jumlah_data_pada_file(self):
        file_path_cari = input('Silahkan Masukkan Nama File : ')
        if os.path.exists('Pertemuan 10' + '/' + file_path_cari + '.txt'):
            with open('Pertemuan 10' + '/' + file_path_cari + '.txt', 'r') as files:
                teks = files.read()
                jumlah = teks.count('+================================================================================')
                jumlah2 = -2 + jumlah
            print('Berhasil')
            print(f'Jumlah Data Pada File : {jumlah2}')
        else:
            print(f'Tidak Terdapat File dengan nama {file_path_cari}.txt')
            print('Jumlah Data Pada File : 0 Data')

    def save_data_pada_file(self):
        teks_file = f'''                             
        +================================================================================
        |Data yang Tersimpan
        +================================================================================
        |Nama      :{self.hasil_nama}
        |Email     :{self.hasil_email}                                                  
        |Password  :{self.hasil_password}
        +================================================================================'''

        tambah_teks_file = f'''
        |Nama      :{self.hasil_nama}
        |Email     :{self.hasil_email}
        |Password  :{self.hasil_password}
        +================================================================================'''

        if self.hasil_email:
            nama_file = input('Silahkan Masukkan nama File : ')
            file_path = 'Pertemuan 10' + '/' + nama_file + '.txt'
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write(teks_file)
                self.hasil_nama = ''
                self.hasil_email = ''
                self.hasil_password = ''
                print('Berhasil')
            else:
                with open(file_path, 'a') as file2:
                    file2.write(tambah_teks_file)
                self.hasil_nama = ''
                self.hasil_email = ''
                self.hasil_password = ''
                print('Berhasil')
        else:
            print('Data saat ini Kosong')

    def buat_data_baru(self):
        nama = input('Silahkan Masukkan Nama Anda : ')
        self.hasil_nama += nama
        while True:
            email = input('Silahkan Masukkan Email Anda : ')
            if self.cek_email(email):
                self.hasil_email += email
                break
            else:
                print("=" * 50)
                print('Email yang Anda Masukkan Salah')
                print("=" * 50)
        while True:
            password = input('Silahkan Masukkan Password Anda : ')
            pattern = (r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d){8,20}')
            if len(password) < 8 or len(password) > 20:
                print("=" * 50)
                print('Password harus memiliki Panjang 8 - 20 karakter')
                print("=" * 50)
            elif not re.match(pattern, password):
                print("=" * 50)
                print('Password yang anda masukkan terlalu lemah')
                print('Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka')
                print("=" * 50)
            else:
                self.hasil_password += password
                break

user = User()

while True:
    print("=" * 50)
    print("Selamat Datang Silahkan Opsi Menu anda")
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Jumlah Data Pada File")
    print("4. Save Data pada File")
    print("5. Buat Data Baru")
    print("6. Keluar")
    opsi = input("Silahkan Pilih Opsi Anda : ")
    print("=" * 50)
    match opsi :
        case '1':
            user.detail_user()
        case '2':
            user.ubah_nama()
        case '3':
            user.jumlah_data_pada_file()
        case '4':
            user.save_data_pada_file()
        case '5':
            user.buat_data_baru()
        case '6':
            print('Sampai Jumpa Lagi')
            break
        case _:
            print("Silahkan coba lagi")
