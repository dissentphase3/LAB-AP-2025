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
            print("Selamat datang silahkan pilih opsi menu anda:")
            print("1. Detail Anda")
            print("2. Ubah Nama")
            print("3. Jumlah Data pada File")
            print("4. Save Data pada File")
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
                self.save_data_pada_file()
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
        print(f"{'=' * 50}")
        nama_file = input("Masukkan nama file tanpa format \".txt\": ")
        try:
            with open(nama_file + ".txt", "r") as file:
                data_lines = file.readlines()
                jumlah_data = sum(1 for line in data_lines if "|Nama:" in line)
                print("Jumlah data pada file : ", f"{jumlah_data} data")
        except FileNotFoundError:
            print("Tidak Terdapat File dengan Nama ", nama_file, ".txt")
            
    def save_data_pada_file(self):
        if not self.data_list:
            print(f"{'=' * 50}")
            print("Data saat ini kosong")
        else:
            print(f"{'=' * 50}")
            nama_file = input("Masukkan nama file tanpa format \".txt\": ")
            file_exists = os.path.isfile(nama_file + ".txt")
            with open(nama_file + ".txt", "a") as file:
                if not file_exists:
                    file.write("+======================================================================+\n")
                    file.write(f"|Data yang tersimpan                                                   \n")
                    file.write("+======================================================================+\n")

                for masukan in self.data_list:
                    file.write(f"|Nama    : {masukan.nama}\n")
                    file.write(f"|Email   : {masukan.email}\n")
                    file.write(f"|Password: {masukan.password}\n")
                    file.write("+======================================================================\n")

            print("Berhasil menyimpan data")
            self.data_list.clear()
    def buat_data_baru(self):
        while True:
            print(f"{'=' * 50}")
            email = input("Masukkan email: ")
            email_pattern = re.compile(r"[a-z0-9.]+@student\.unhas\.ac\.id$")
            if not email_pattern.match(email):
                print("Email yang Anda Masukkan Salah")
                continue
            else:
                break
          
        while True:  
            password = input("Masukkan password: ")
            password_length = len(password)
            password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,20}$")
            if password_length < 8 or password_length > 20 :
                print("Password harus memiliki Panjang 8 – 20 karakter dan minimal 1 huruf kapital, huruf kecil, dan angka")
                continue
            elif not password_pattern.match(password):
                print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 hruf kapital, huruf kecil, dan angka")
                continue
            else:
                break  
        nama = input("Masukkan nama: ")
        new_data = Data()
        new_data.nama = nama
        new_data.email = email
        new_data.password = password
        self.data_list.append(new_data)
program = Program()
program.menu()