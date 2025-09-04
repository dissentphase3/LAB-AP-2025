class Mahasiswa:
    def __init__(self, nama, nim, jurusan, IPK):
        self.__nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = IPK
    def set_nama(self, nama):
        self.__nama = nama
    def get_nama(self):
        return self.__nama

    def Tampilkan_info(self):
        print(f"Nama\t\t: {self.__nama}\nNIM\t\t: {self.nim}\nJurusan\t\t: {self.jurusan}\nIPK\t\t: {self.ipk}")
    
    def Hitung_predikat(self):
        nilai = self.ipk
        predikat = ""
        if nilai < 2 :
            predikat += "Kurang"
        elif nilai < 2.5 :
            predikat += "Cukup"
        elif nilai < 3.0 :
            predikat += "Memuaskan"
        elif nilai < 3.5 :
            predikat += "Sangat memuaskan"
        elif nilai <= 4.0 :
            predikat += "Cumlaude"
        elif nilai < 0 or nilai > 4:
            predikat += "Input Salah! IPK hanya dalam rentan 0-4 !!!"
        print(f"Predikat\t: {predikat}")

saya = Mahasiswa("Ananta Waskita Gisda", "H071231007", "Sistem Informasi", 3.9)
saya.Tampilkan_info()
saya.Hitung_predikat()


