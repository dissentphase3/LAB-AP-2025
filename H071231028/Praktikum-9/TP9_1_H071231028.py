class Human:
    def __init__(self, name, position, speed=1):
        self.nama = name
        self.__posisi = position 
        self._speed = speed

    def movement(self, arah):
        for move in arah:
            if move == 'L':
                self.__posisi  -= self._speed
            elif move == 'R':
                self.__posisi  += self._speed

    def setPosisi(self, position):
        self.__posisi = position

    def getPosisi(self):
        return self.__posisi

    def setSpeed(self, speed):
        self._speed = speed

    def getSpeed(self):
        return self._speed

class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        # target._health = target._health - self._power
        target.setHealth (target.getHealth()-self.getPower())
        return target._health

    def setPower(self, power):
        self._power = power

    def getPower(self):
        return self._power

    def setHealth(self, health):
        self._health = health

    def getHealth(self):
        return self._health

    def setArmor(self, armor):
        self._armor = armor

    def getArmor(self):
        return self._armor

    

class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._armor = 45
        self._power = 32
        target.setHealth(target.getHealth()- self.getPower())

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._speed = 7
        self._power = 42
        target.setHealth (target.getHealth() - self.getPower())

class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target.setHealth (target.getHealth() + 150)

