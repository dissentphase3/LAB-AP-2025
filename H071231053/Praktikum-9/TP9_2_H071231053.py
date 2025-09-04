class mahasiswa :

    def __init__(self,nama,nim,jurusan,ipk) :
        self.__nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self) :
        print(f"Nama Mahasiswa : {self.__nama}\nNIM            : {self.nim}\nJurusan        : {self.jurusan} \nIPK            : {self.ipk}")



    def Hitung_predikat(self) :
        if self.ipk >= 3.5 :
            print("Cumlaude")
        elif self.ipk >= 3.0 :
            print("Sangat Memuaskan")
        elif self.ipk >= 2.5 :
            print ("Memuaskan")
        elif self.ipk >= 2.0 :
            print ("Cukup")
        elif self.ipk < 2.0 :
            print ("kurang")

    def setnama(self,nama):
        self.__nama = nama
    def getnama(self):
        return self.__nama
    

a = mahasiswa("Asep","H071231099","Sisfo",3.0)
a.tampilkan_info()
a.Hitung_predikat()


