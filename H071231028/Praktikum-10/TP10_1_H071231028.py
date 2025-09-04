import re
import os

class Data:
    def __init__(self):
        self.nama = ""
        self.email = ""
        self.password = ""

class Program:
    def __init__(self):
        self.data = Data()
        self.data_list = []

    def menu(self):
        while True:
            print(f"{'=' * 50}")
            print("Selamat datang! Silakan pilih opsi menu:")
            print("1. Detail Anda")
            print("2. Ubah Nama")
            print("3. Jumlah Data pada File")
            print("4. Simpan Data pada File")
            print("5. Buat Data Baru")
            print("6. Keluar")

            pilihan = input("Masukkan pilihan: ")

            if pilihan == "1":
                self.detail_anda()
            elif pilihan == "2":
                self.ubah_nama()
            elif pilihan == "3":
                self.jumlah_data_pada_file()
            elif pilihan == "4":
                self.simpan_data_pada_file()
            elif pilihan == "5":
                self.buat_data_baru()
            elif pilihan == "6":
                print("Sampai Jumpa Lagi")
                break
            else:
                print("Pilihan tidak valid")

    def detail_anda(self):
        if not self.data_list:
            print(f"{'=' * 50}")
            print("Data saat ini kosong")
        else:
            print(f"{'=' * 50}")
            latest_data = self.data_list[-1]
            print("Detail Anda:")
            print("Nama    : ", latest_data.nama)
            print("Email   : ", latest_data.email)
            print("Password: ", latest_data.password)

    def ubah_nama(self):
        if not self.data_list:
            print(f"{'=' * 50}")
            print("Data saat ini kosong")
        else:
            print(f"{'=' * 50}")
            nama_baru = input("Masukkan nama baru: ")
            self.data_list[-1].nama = nama_baru
            print("Nama berhasil diubah")

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

    def check_and_create_file(self, nama_file):
        file_exists = os.path.isfile(nama_file + ".txt")
        with open(nama_file + ".txt", "a") as file:
            if not file_exists:
                file.write("+======================================================================|\n")
                file.write(f"|Data yang tersimpan                                                  | \n")
                file.write("+=======================================================================\n")

    def save_data_to_file(self, nama_file):
        with open(nama_file + ".txt", "a") as file:
            for masukan in self.data_list:
                file.write(f"|Nama    : {masukan.nama}\n")
                file.write(f"|Email   : {masukan.email}\n")
                file.write(f"|Password: {masukan.password}\n")
                file.write("+======================================================================\n")

    def validate_email(self, email):
        email_pattern = re.compile(r"[a-z0-9.]+@student\.unhas\.ac\.id$")
        return bool(email_pattern.match(email))

    def validate_password(self, password):
        password_length = len(password)

        if not (8 <= password_length <= 20):
            print("Password harus memiliki Panjang 8 – 20 karakter")
            return False

        if not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
            print("Password yang Anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, 1 huruf kecil, dan 1 angka")
            return False

        return True

    def buat_data_baru(self):
        print(f"{'=' * 50}")
        nama = input("Masukkan nama: ")

        while True:
            email = input("Masukkan email: ")
            if self.validate_email(email):
                break
            else:
                print("Email yang Anda Masukkan Salah.")

        while True:
            password = input("Masukkan password: ")
            if self.validate_password(password):
                break

        new_data = Data()
        new_data.nama = nama
        new_data.email = email
        new_data.password = password
        self.data_list.append(new_data)
        print(f"{'=' * 50}")
        print("Data berhasil ditambahkan.")

    def simpan_data_pada_file(self):
        if not self.data_list:
            print(f"{'=' * 50}")
            print("Data saat ini kosong")
        else:
            print(f"{'=' * 50}")
            nama_file = input("Masukkan nama file tanpa format \".txt\": ")
            self.check_and_create_file(nama_file)
            self.save_data_to_file(nama_file)
            print(f"{'=' * 50}")
            print("Berhasil menyimpan data ke file.")
            self.data_list.clear()

# Program Utama
program = Program()
program.menu()
