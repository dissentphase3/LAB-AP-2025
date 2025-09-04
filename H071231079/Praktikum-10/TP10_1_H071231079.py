import re
import os

class UserData:
    def __init__(self):
        self.nama = ""
        self.email = ""
        self.password = ""

    def display_data(self):
        if self.nama == "":
            print("Data saat ini kosong")
        else:
            print("Data Anda Adalah : ")
            print(f"Nama     : {self.nama}")
            print(f"Email    : {self.email}")
            print(f"Password : {self.password}")

    def validasi_email(self, email):
        pattern = r'^[a-z0-9.]+@student\.unhas\.ac\.id$'
        return re.search(pattern, email)

    def validasi_password(self, password):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{8,20}$'
        return re.search(pattern, password)

    def ubah_nama(self):
        if self.nama == "":
            print("Data saat ini kosong")
        else:
            new_name = input("Silahkan Input Nama Baru : ")
            self.nama = new_name

    def jumlah_data_pada_file(self):
        file_name = input("Silahkan Masukkan Nama File : ")
        if not os.path.exists(f"{file_name}.txt"):
            print(f"Tidak Terdapat File dengan Nama {file_name}.txt")
            print("=" * 60)
        else:
            with open(f"{file_name}.txt", "r") as file:
                lines = len(file.readlines())
                jumlah_data = (lines - 3) // 4
                print(f"Jumlah Data pada File {file_name}.txt : {jumlah_data} Data")

    def save_data_pada_file(self):
        if self.nama == "":
            print("Data saat ini kosong")
        else:
            file_name = input("Silahkan Masukkan Nama File : ")
            if not os.path.exists(f"{file_name}.txt"):
                with open(f"{file_name}.txt", "w") as file_up:
                    file_up.write(f"+" + "=" * 68 + "+\n")
                    file_up.write("|" + "Data Yang Tersimpan\n")
                    file_up.write(f"+" + "=" * 68 + "+")
            with open(f"{file_name}.txt", "a") as file_data:
                file_data.write(f"\n|" + "Nama             : " + self.nama)
                file_data.write(f"\n|" + "Email            : " + self.email)
                file_data.write(f"\n|" + "Password         : " + self.password)
                file_data.write(f"\n+" + "=" * 68 + "+")    
            print("Berhasil Menyimpan Data")
            self.nama = ""
            self.email = ""
            self.password = ""

    def buat_data(self):
        self.nama = input("Silahkan Masukkan Nama Anda     : ")
        while True:
            self.email = input("Silahkan Masukkan Email Anda    : ")
            if not self.validasi_email(self.email):
                print("=" * 60 + "\nEmail yang Anda Masukkan Salah\n" + "=" * 60)
            else:
                break
        while True:
            self.password = input("Silahkan Masukkan Password Anda : ")
            if not 8 <= len(self.password) <= 20:
                print("=" * 60 + "\nPassword Harus Memiliki Panjang 8-20\n" + "=" * 60)
            elif not self.validasi_password(self.password):
                print("=" * 60 + "\nPassword yang Anda Masukkan terlalu lemah")
                print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka\n" + "=" * 60)
            else:
                break

menu_data = UserData()

while True:
    print("=" * 60)
    print("Selamat Datang Silahkan Pilih Opsi Menu Anda!")
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Jumlah Data pada File")
    print("4. Save Data pada File")
    print("5. Buat Data Baru")
    print("6. Keluar")
    print("=" * 60)

    opsi = input("Silahkan Pilih Opsi Anda : ")
    print("=" * 60)

    match opsi:
        case "1" :
            menu_data.display_data()
        case "2" :
            menu_data.ubah_nama()
        case "3" :
            menu_data.jumlah_data_pada_file()
        case "4" :
            menu_data.save_data_pada_file()
        case "5":
            menu_data.buat_data()
        case "6" :
            print("Sampai Jumpa Lagi".center(60))
            print("=" * 60)
            break
        case _:
            print("Pilihan tidak valid. Silakan pilih kembali.")
            continue