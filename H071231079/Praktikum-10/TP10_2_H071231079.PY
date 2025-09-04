class Pegawai:
    def __init__(self, nama, usia, alamat, lamaBekerja, status):
        self._nama = nama
        self._usia = usia
        self._alamat = alamat
        self._lamaBekerja = lamaBekerja
        self._status = status
        self._gaji = self.hitung_gaji()

    def hitung_gaji(self):
        pass

    def detail(self):
        pass

    def get_nama(self):
        return self._nama
    
    def get_usia(self):
        return self._usia
    
    def get_alamat(self):
        return self._alamat
    
    def get_lamaBekerja(self):
        return self._lamaBekerja
    
    def get_status(self):
        return self._status
    
    def get_gaji(self):
        return self._gaji

    def set_gaji(self, gaji_baru):
        self._gaji = gaji_baru

class PegawaiTetap(Pegawai):
    def hitung_gaji(self):
        return 5000000 + self._lamaBekerja * 1000000

    def detail(self):
        return f"""{"=" * 60}
{"PEGAWAI TETAP".center(60)}
{"=" * 60} 
Nama         : {self._nama} 
Usia         : {self._usia} 
Alamat       : {self._alamat} 
Lama Bekerja : {self._lamaBekerja} tahun 
Status       : {self._status} 
Gaji         : {self._gaji}"""
    
class PegawaiKontrak(Pegawai):
    def __init__(self, nama, usia, alamat, lamaBekerja, status):
        super().__init__(nama, usia, alamat, lamaBekerja, status)
        if self._lamaBekerja >= 3:
            self.__class__ = PegawaiTetap
            self._gaji = self.hitung_gaji()

    def hitung_gaji(self):
        return 3000000 + self._lamaBekerja * 900000  # Menaikkan gaji untuk pegawai kontrak yang diubah menjadi tetap

    def detail(self):
        return f"""{"=" * 60}
{"PEGAWAI KONTRAK".center(60)} 
{"=" * 60}
Nama         : {self._nama} 
Usia         : {self._usia} 
Alamat       : {self._alamat} 
Lama Bekerja : {self._lamaBekerja} tahun 
Status       : {self._status} 
Gaji         : {self._gaji}"""
    
# Membuat objek PegawaiKontrak dengan lama bekerja < 3 tahun
pegawai_kontrak1 = PegawaiKontrak("Nera", 22, "Onta Lama", 2, "Menikah")
print(pegawai_kontrak1.detail())  

# Membuat objek PegawaiKontrak dengan lama bekerja >= 3 tahun
pegawai_kontrak2 = PegawaiKontrak("Jasmine", 23, "Baruga", 3, "Belum Menikah")
print(pegawai_kontrak2.detail())  

# Membuat objek PegawaiTetap dengan lama bekerja >= 3 tahun
pegawai_tetap1 = PegawaiTetap("Lia", 23, "BTP Blok A", 4, "Belum Menikah")
print(pegawai_tetap1.detail()) 