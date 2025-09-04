import os; os.system('clear')

from time import sleep
# Kelas abstrak
class Car:
    def __init__(self, nama, tahun, speed):
        self.__nama = nama
        self.__tahun = tahun
        self.__speed = speed

    def setNama(self, nama):
        self.__nama = nama

    def getNama(self):
        return self.__nama
    
    def setTahun(self, tahun):
        self.__nama = tahun

    def getTahun(self):
        return self.__tahun
    
    def setSpeed(self, speed):
        self.__speed = speed

    def getSpeed(self):
        return self.__speed

    def NOS(self):
        pass

    def tampilkanInfo(self):
        return f"\nName      : {self.__nama}\nYear      : {self.__tahun}\nSpeed     : {self.__speed} km/h"

class SportCar(Car):
    def __init__(self, nama, tahun, speed):
        super().__init__(nama, tahun, speed)

    def tampilkanInfo(self):
        return f"{super().tampilkanInfo()}"
    
    def startEngine(self):
        return f"\nStarting the engine for {self.getNama()}"

    def stopEngine(self):
        return f"\nStopping the engine for {self.getNama()}"

    def NOS(self): # Tambahan 150HP (berat mobil diabaikan)
        daya = 37285 ; t = 3; m = self.getSpeed() * t / 3600 * 1000
        kecepatanNOS = ((2 * daya) / m) ** 0.5
        newSpeed = self.getSpeed() + kecepatanNOS
        print(f'\n{self.getNama()} uses NOS\nCurrent {self.getNama()} speed: {round(newSpeed, 2)} km/h')
        for i in range(3+1):
            print(i, end='\r')
            sleep(1)
        print('NOS have been used up.')
    
    def upgradeEngine(self):
        self.setSpeed(self.getSpeed() + 10)
        print(f"\n{self.getNama()} has been upgraded.")