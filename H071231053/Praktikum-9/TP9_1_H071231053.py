class Human:
    def __init__(self, name, pos_x=None):
        self.name = name
        self.__position = pos_x
        self._speed = None

    def movement(self, arah):
        if self.__position is not None and self._speed is not None:
            for i in arah :
                if i == "L":
                    self.__position -= self._speed
                    
                elif i == "R":
                    self.__position += self._speed
                    

    def setSpeed(self, speed):
        self._speed = speed
    def getSpeed(self):
        return self._speed

    def setPosition(self, pos_x=None):
        self.__position = pos_x
    def getPosition(self):
        return self.__position


class Hero(Human):
    def __init__(self, name, pos_x=None):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self.setSpeed(3)

    def setPower(self, power):
        self._power = power
    def getPower(self):
        return self._power

    def setArmor(self, armor):
        self._armor = armor
    def getArmor(self):
        return self._armor

    def setHealth(self, health):
        self._health = health
    def getHealth(self):
        return self._health

    def attack(self, target):
        target.setHealth(target.getHealth() - self._power)


class Warrior(Hero):
    def __init__(self, name, pos_x=None):
        super().__init__(name, pos_x)
        self.setPower(26)
        self.setArmor(30)

    def special(self, target):
        self.setArmor(45)
        self.setPower(32)
        target.setHealth(target.getHealth() - self.getPower())


class Assasin(Hero):
    def __init__(self, name, pos_x=None):
        super().__init__(name, pos_x)
        self.setPower(35)
        self.setSpeed(4)

    def special(self, target):
        self.setSpeed(7)
        self.setPower(42)
        target.setHealth(target.getHealth() - self.getPower())

class Support(Hero):
    def __init__(self, name, pos_x=None):
        super().__init__(name, pos_x)
        self.setHealth(500)
        self.setArmor(8)
        self.setSpeed(4)

    def special(self, target):
        self._speed = 6
        target.setHealth(target.getHealth() + 150)

