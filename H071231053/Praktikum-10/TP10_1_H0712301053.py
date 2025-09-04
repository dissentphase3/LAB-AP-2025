import re
import os

data = []

class Akun :
    def __init__(self,nama,email,password) :
        self.nama = nama
        self.email = email
        self.password = password

    def detail(self):
        print(f"""
------------------------------------------------------------
        Nama     : {self.nama}
        Email    : {self.email}
        Password : {self.password}
------------------------------------------------------------
""")

    def data_baru(self):
        data.append(nama)
        data.append(email)
        data.append(password)
        print(f"""
------------------------------------------------------------
            Data telah terupdate
------------------------------------------------------------
""")

    def ubah_nama(self):
        nama = input("Masukkan Nama Baru : ")
        data[0] = nama
        self.nama = nama
        print(f"""
------------------------------------------------------------
            Nama berhasil diubah
------------------------------------------------------------
""")

    def save(self):
        file = input()
        x = file + ".txt"
        if not os.path.exists(x) :
            with open(x,"w") as files :
                files.write(f"""
-------------------------------------------------------
|Data Tersimpan
-------------------------------------------------------
                            """)
        with open(x,"a") as files :
            files.write(f"""
--------------------------------------------------------
|{'nama'.ljust(9)}: {self.nama}
|{'Email'.ljust(9)}: {self.email}
|{'Password'.ljust(9)}: {self.password}
--------------------------------------------------------
                        """)
        data.clear()
        self.nama = None
        self.email = None
        self.password = None
        print(f"""
-----------------------------------------------
Berhasil Menyimpan data
-----------------------------------------------
""")  

print(f"""
-----------------------------------------------------
Selamat Datang
-----------------------------------------------------
""")

while True :
    print(f"""
-----------------------------------------------------
1. Detail Anda
2. Ubah Nama
3. jumlah data pada file
4. Save Data pada File
5. Buat Data Baru
6. Keluar
-----------------------------------------------------
""")
    pilihan = input("Silahkan Input Opsi Anda : ")
    print("---------------------------------------------------")

    match pilihan :

        case "1":
            if data == [] :
                print(f"""
---------------------------------------------------------
                      Data Kosong
---------------------------------------------------------
""")
            else :
                ac.detail()

        case "2":
            if data == [] :
                print(f"""
---------------------------------------------------------
                      Data Kosong
---------------------------------------------------------
""")
            else :
                ac.ubah_nama()

        case "3":
            file = input("Masukkan Nama File yang ingin dicari : ")
            cari = file + ".txt"
            if not os.path.exists(cari):
                print(f"""
---------------------------------------------------------
                      File {cari} tidak ditemukan
---------------------------------------------------------
""")
            else :
                with open(cari,"r") as files :
                    x = files.read()
                    hitung = x.count("nama")
                    print(f"""
---------------------------------------------------------
terdapat {hitung} data dalam {cari}
---------------------------------------------------------
""")

        case "4":
            if data == [] :
                print(f"""
Data Kosong
---------------------------------------------------------""")
            else :
                ac.save()

        case "5":
            nama = input("Masukkan Nama : ")

            while True :
                email = input("Masukkan Email : ")
                patt = r"^[a-z]+[0-9]{2,}+@student\.unhas\.ac\.id$"
                if re.match(patt,email):
                    break
                else :
                    print(f"""
-----------------------------------------------------
Email yang anda Masukkan Salah
-----------------------------------------------------
""")
                
            while True :
                password = input("Masukkan Password : ")
                patt = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$"
                if len(password) < 8 or len(password) > 20 :
                    print(f"{'='*100}\nPassword Harus Memiliki panjang 8-20\n{'='*100}")
                else :
                    if re.match(patt,password):
                        break
                    else :
                        print(f"""
--------------------------------------------------
Password Yang anda masukkan terlalu lemah
Gunakan minimal 1 huruf kapital,huruf kecil dan angka
-------------------------------------------------
""")

            ac = Akun(nama,email,password)
            ac.data_baru()

        case "6":
            print(f"""
Selamat Tinggal
------------------------------------------------
                  """)
            break

        case _:
            print(f"Input Diluar Opsi\n{'='*100}")
            