class Kartun:
    def __init__(self, judul, usia, jenis, episode_terakhir):
        self._judul = judul
        self._usia = usia
        self._jenis = jenis
        self._episode_terakhir = episode_terakhir
        self._rating = self.hitung_rating()

    def hitung_rating(self):
        pass

    def detail(self):
        pass

    def get_nama(self):
        return self._nama

    def get_usia(self):
        return self._usia

    def get_jenis(self):
        return self._jenis

    def get_episode_terakhir(self):
        return self._episode_terakhir

    def get_rating(self):
        return self._rating

    def set_rating(self, rating_baru):
        self._rating = rating_baru


class KartunAnak(Kartun):
    def hitung_rating(self):
        return 4.5 + self._episode_terakhir * 0.1

    def detail(self):
        return f"""{"=" * 60}
{"KARTUN ANAK".center(60)}
{"=" * 60} 
Judul Kartun      : {self._judul} 
Usia              : {self._usia} 
Jenis Kartun      : {self._jenis} 
Episode Terakhir  : {self._episode_terakhir} 
Rating            : {self._rating}"""


class KartunRemaja(Kartun):
    def __init__(self, judul, usia, jenis, episode_terakhir, tema_remaja):
        super().__init__(judul, usia, jenis, episode_terakhir)
        self._tema_remaja = tema_remaja

    def hitung_rating(self):
        return 4.0 + self._episode_terakhir * 0.08

    def detail(self):
        return f"""{"=" * 60}
{"KARTUN REMAJA".center(60)}
{"=" * 60}
Judul kartun      : {self._judul} 
Usia              : {self._usia} 
Jenis Kartun      : {self._jenis} 
Episode Terakhir  : {self._episode_terakhir} 
Tema Remaja       : {self._tema_remaja} 
Rating            : {self._rating}"""


# Membuat objek KartunAnak
kartun_anak = KartunAnak("Doraemon", 8, "Animasi", 100)
print(kartun_anak.detail())

# Membuat objek KartunRemaja
kartun_remaja = KartunRemaja("One Piece", 16, "Anime", 100, "Petualangan")
print(kartun_remaja.detail())
