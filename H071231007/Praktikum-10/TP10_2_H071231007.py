from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def hitungLuas(self):
        pass
    def keliling(self) :
        pass

class Segitiga(Bentuk) :
    def __init__(self,tinggi,alas) :
        self._tinggi = tinggi
        self._alas = alas
    
    def setTinggi (self,tinggi) :
        self._tinggi = tinggi
    def setAlas (self,alas) :
        self._alas = alas
    
    def getTinggi(self):
        print(self._tinggi)
    def getAlas(self):
        print(self._alas)

    def hitungLuas(self) :
        print (1/2 * self._alas * self._tinggi)
    def keliling(self) :
        c = (self._tinggi**2 + self._alas**2)**(1/2)
        print(f'{self._alas + self._tinggi + c:.2f}')
    
class SegiEmpat(Bentuk) :
    def __init__(self,sisi) :
        self._sisi = sisi

    def setTinggi (self,sisi) :
        self._sisi = sisi   
    def getTinggi(self):
        print(self._sisi)

    def hitungLuas(self) :
        print(self._sisi * self._sisi)
    def keliling(self):
        print(self._sisi * 4)


#method interface
def luas(Bentuk):
    Bentuk.hitungLuas()
def keliling(Bentuk) :
    Bentuk.keliling()


segitiga = Segitiga(12,4)
segiempat = SegiEmpat (8)
# segitiga.keliling()
# segiempat.keliling()
# segitiga.hitungLuas()
# segiempat.hitungLuas()
luas(segitiga)
luas(segiempat)
keliling(segitiga)
keliling(segiempat)

