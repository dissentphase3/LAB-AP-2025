class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkanInfo(self):
        print(f'Nama      : {self.nama.title()}\nNIM       : {self.nim.upper()}\nJurusan   : {self.jurusan.title()}\nIPK       : {self.ipk}')
    
    def hitungPredikat(self):
        if self.ipk > 4 or self.ipk < 0:
            print('IPK di luar jangkauan!')
        elif 3.5 <= self.ipk <= 4:
            print('Predikat  : Cumlaude')
        elif self.ipk >= 3:
            print('Predikat  : Sangat memuaskan')
        elif self.ipk >= 2.5:
            print('Predikat  : Memuaskan')
        elif self.ipk >= 2:
            print('Predikat  : Cukup')
        else:
            print('Predikat  : Kurang')
