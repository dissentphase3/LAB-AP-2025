class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkanInfo(self):
        print("Nama     = ", self.nama)
        print("NIM      = ", self.nim)
        print("Jurusan  = ", self.jurusan)
        print("IPK      = ", self.ipk)
    
    def hitungPredikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Cukup"
        else: 
            return "Kurang"

mahasiswa1 = Mahasiswa("Lia", "H071231079", "Sistem Informasi", 4.0)
mahasiswa1. tampilkanInfo()
print("Predikat =",  mahasiswa1.hitungPredikat())