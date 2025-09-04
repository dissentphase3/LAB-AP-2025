class Pasien():
    def __init__(self, id, nama, alergi):
        self._id = id
        self._nama = nama
        self._alergi = alergi

class PasienRawatInap(Pasien):
    def __init__(self, id, nama, alergi, nomor_ruang=None, lama_rawat=3, kondisi_baik=True, kondisi_buruk=False):
        super(PasienRawatInap, self).__init__(id, nama, alergi)
        self._nomor_ruang = nomor_ruang
        self._lama_rawat = lama_rawat
        self.kondisi_baik = kondisi_baik
        self.kondisi_buruk = kondisi_buruk

    def kondisi_membaik(self):
        if not self.kondisi_baik:
            self._lama_rawat -= 2
            self.kondisi_baik = True
            self.kondisi_buruk = False
            print('{} telah membaik. Lama rawat menjadi {} hari.'.format(self._nama, self._lama_rawat))
        else:
            print('{} sudah dalam kondisi baik sebelumnya.'.format(self._nama))

    def kondisi_memburuk(self):
        if not self.kondisi_buruk:
            self._lama_rawat += 7
            self.kondisi_baik = False
            self.kondisi_buruk = True
            print('{} mengalami pemburukan kondisi. Lama rawat menjadi {} hari.'.format(self._nama, self._lama_rawat))
        else:
            print('{} sudah dalam kondisi buruk sebelumnya.'.format(self._nama))

    def get_info(self):
        return {
            'ID': self._id,
            'Nama': self._nama,
            'Alergi': self._alergi,
            'Nomor Ruang': self._nomor_ruang,
            'Lama Rawat': self._lama_rawat,
            'Kondisi Baik': self.kondisi_baik,
            'Kondisi Buruk': self.kondisi_buruk
        }
class RumahSakit():
    def __init__(self, nama, kapasitas):
        self._nama = nama
        self._pasien = []
        self._kapasitas = kapasitas

    def admit(self, pasien_rawat_inap):
        if len(self._pasien) >= self._kapasitas:
            print('Maaf! Rumah Sakit penuh! Tidak dapat menerima pasien baru.')
        else:
            self._pasien.append(pasien_rawat_inap)
            print('{} telah dirawat selama {} hari.'.format(pasien_rawat_inap._nama, pasien_rawat_inap._lama_rawat))

    def pulang(self, nama):
        for pasien_rawat_inap in self._pasien:
            if pasien_rawat_inap._nama == nama:
                if pasien_rawat_inap.kondisi_baik:
                    print('{} telah pulang setelah dirawat selama {} hari.'.format(nama, pasien_rawat_inap._lama_rawat))
                    self._pasien.remove(pasien_rawat_inap)
                elif pasien_rawat_inap.kondisi_buruk:
                    print('Maaf, {} belum bisa pulang karena kondisinya masih buruk.'.format(nama))
                else:
                    print('{} belum bisa pulang karena kondisinya tidak jelas.'.format(nama))
                    
pasien1 = PasienRawatInap(id=1, nama="Jokowi", alergi="Tidak Ada", nomor_ruang="101")
pasien2 = PasienRawatInap(id=2, nama="Chandra", alergi="kucing")
pasien3 = PasienRawatInap(id=3, nama="Gibran", alergi="Twitter", nomor_ruang="102")

rumah_sakit = RumahSakit(nama="RS Sehat", kapasitas=2)

rumah_sakit.admit(pasien1)
rumah_sakit.admit(pasien2)
rumah_sakit.admit(pasien3)

pasien2.kondisi_memburuk()

print("Pasien Saat Ini di {}:".format(rumah_sakit._nama))
for pasien in rumah_sakit._pasien:
    print(pasien.get_info())

rumah_sakit.pulang("Jokowi")
pasien3.get_info

print("Pasien Saat Ini di {}:".format(rumah_sakit._nama))
for pasien in rumah_sakit._pasien:
    print(pasien.get_info())  
