from abc import ABC, abstractmethod

class Mobil(ABC):
    def __init__(self,nama):
        self.__nama = nama
    @abstractmethod
    def suara(self):
        pass
    def get_nama(self):
        return self.__nama
    def set_nama(self,nama):
        self.__nama = nama
        
    
class Bmw(Mobil):
    def suara(self):
        return "bang aku bole ngebut ga?"

class Koenigsegg(Mobil):
    def suara(self):
        return "aku mah masi pemula (439km/h)"

B = Bmw("Bmw ngeeng I8 gon brom brom")
K = Koenigsegg("gwehj ketika agera berkutik")

print(f'{B.suara()}')
print(f'{K.suara()}')
