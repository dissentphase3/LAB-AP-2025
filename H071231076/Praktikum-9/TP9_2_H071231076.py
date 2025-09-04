class Mahasiswa :
    def __init__(self, nama, nim, jurusan, ipk) :
        self.Nama = nama
        self.Nim = nim
        self.Jurusan = jurusan
        self.Ipk = ipk
    def tampilkan_info(self):
        print(f"Nama : {self.Nama}")
        print(f"NIM : {self.Nim}")
        print(f"Jurusan : {self.Jurusan}")
        print(f"IPK : {self.Ipk}")
    def hitung_predikat(self):
        if self.Ipk >= 3.5 :
            print ("Cumlaude")
        elif self.Ipk >= 3.0 :
            print ("Sangat Memuaskan")
        elif self.Ipk >= 2.5 :
            print ("Memuaskan" )
        elif self.Ipk >= 2.0 :
            print ("Cukup")
        else :
            print ("Kurang")

Mahasiswa1 = Mahasiswa("Adrian Tri Putra", "H071231076", "Sistem Informasi", 4.0)
Mahasiswa1.tampilkan_info()
Mahasiswa1.hitung_predikat()

  