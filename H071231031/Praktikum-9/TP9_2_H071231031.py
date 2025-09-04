class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan 
        self.ipk  = ipk

    def tampilkan_info(self):
        print(f'''
Nama     = {self.nama}
NIM      = {self.nim}
Jurusan  = {self.jurusan}
IPK      = {self.ipk}''')
    def hitung_predikat(self):
        predikat = ""
        if self.ipk >= 3.5:
            predikat += "Cumlaude"
        elif self.ipk >= 3.0:
            predikat += "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            predikat += "Memuaskan"
        elif self.ipk >= 2.0:
            predikat += "Cukup"
        else:
            predikat += "Kurang"
        
        print(f'Predikat = {predikat}')

nama = "Naufal"
nim = "H071231031"
jurusan = "Sistem Informasi"
ipk = 4.0
mahasiswa = Mahasiswa(nama, nim, jurusan, ipk)
mahasiswa.tampilkan_info()
mahasiswa.hitung_predikat()