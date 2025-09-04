class Human:
    def __init__ (self,name,pos_x,speed=1):
        self.name = name
        self.__position = pos_x
        self._speed = speed
    
    def movement(self,arah):
        for i in arah:
            if i == 'L':
                self.__position = self.__position - self._speed
            elif i == 'R':
                self.__position = self.__position+ self._speed
    def setPosition(self, pos_x):
        self.__position = pos_x
    def getPosition(self):
        return self.__position
  
class Hero(Human):
    def __init__ (self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
        
    def attack(self,target):
        target._health = target._health - self._power
    
    def setHealth(self,health):
        self._health = health
    def getHealth(self):
        return self._health
    
    def setSpeed(self,speed):
        self._speed = speed
    def getSpeed(self):
        return self._speed
    
    def setpower(self,power):
        self._power = power
    def getpower(self):
        return self._power
    
    def setarmor(self,armor):
        self._armor = armor
    def getarmor(self):
        return self._armor
    
class Warrior(Hero):
    def __init__ (self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 26
        self._armor = 30
    
    def special(self,target):
        print('Sedang menggunakan Special Skill')
        self._armor = 45
        self._power = 32
        # target._health = target._health - self._power
        target.setHealth(target.getHealth() - self._power)
        
class Assassin(Hero):
    def __init__ (self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 35
        self._speed = 4
    
    def special(self,target):
        print('Sedang menggunakan Special Skill')
        self._speed = 7
        self._power = 42
        # target._health = target._health - self._power
        target.setHealth(target.getHealth() - self._power)
        
class Support(Hero):
    def __init__ (self,name,pos_x):
        super().__init__(name,pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4
    
    def special(self,target):
        print('Sedang menggunakan Special Skill')
        self._speed = 6
        # target._health = target._health + 150
        target.setHealth(target.getHealth() + 150)


