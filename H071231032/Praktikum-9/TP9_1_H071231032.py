deadMan = []

class Human:
    def __init__(self, name, pos_x):
        self.name = name
        self.__pos_x = int(pos_x)
        self._speed = 1

    def setPos_x(self, posx):
        self.__pos_x = posx
        
    def getPos_x(self):
        return self.__pos_x
    
    def setSpeed(self, speed):
        self._speed = speed

    def getSpeed(self):
        return self._speed

    def movement(self, arah):
        if self.getHealth() <= 0: print(f"{self.name} can't move!")
        for i in str(arah):
            if i == 'L':
                self.__pos_x -= self._speed
            elif i == 'R':
                self.__pos_x += self._speed

class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
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
        if self.getHealth() > 0:
            target.setHealth(target.getHealth() - self.getPower())
            if target.getHealth() <= 0:
                target.setHealth(0)
                target.setPower(0)
                target.setArmor(0)
                target.setSpeed(0)
                Hero.messenge(target.name)
        else: print(f"{self.name} can't attack!")

    def messenge(x):
        if x not in deadMan:
            print(f"{x} has been slain!")
            deadMan.append(x)
        else: pass

class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def special(self, target):
        if self.getHealth() <= 0: print(f"{self.name} can't use his special!")
        else:
            self._power = 32
            self._armor = 45
            self.attack(target)

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4
    
    def special(self, target):
        if self.getHealth() <= 0: print(f"{self.name} can't use his special!")
        else:
            self._power = 42
            self._speed = 7
            self.attack(target)

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4
    
    def special(self, target):
        if self.getHealth() <= 0: print(f"{self.name} can't use his special!")
        else:
            self._speed = 6
            target.setHealth(target.getHealth() + 150)