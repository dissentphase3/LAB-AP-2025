class Human :
    def __init__(self, name, position, speed=1):
        self.name = name
        self._speed = speed
        self.__position = position

    def movement(self, direct):
        for i in direct:
           if i == "L":
                self.__position -= self._speed
                print(f"[{self.name.title()}] moved, now [{self.name.title()}] was on {self.__position}")
           elif i == "R":
                self.__position += self._speed
                print(f"[{self.name.title()}] moved, now [{self.name.title()}] was on {self.__position}")

    def set_position(self, position):
        self.__position = position
    
    def get_position(self):
        return self.__position
    
class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.set_position(position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target._health -= self._power
        print(f"[{self.name.title()}] attacked [{target.name.title()}] deals {self._power} damage, [{target.name.title()}] health {target._health} left")

    def set_power(self, power):
        self._power = power

    def get_power(self):
        return self._power
    
    def set_health(self, health):
        self._health = health

    def get_health(self):
        return self._health
    
    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed
    
    def set_armor(self, armor):
        self._armor = armor

    def get_armor(self):
        return self._armor

class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.set_position(position)
        self._power = 26
        self._armor = 30
        
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power
        print(f"[{self.name.title()}] use special skill and deals {self._power} damage! [{target.name.title()}] health {target._health} left")

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.set_position(position)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._power = 42
        self._speed = 7
        target._health -= self._power
        print(f"[{self.name.title()}] use special skill and deals {self._power} damage! [{target.name.title()}] health {target._health} left")

class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.set_position(position)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health += 150
        print(f"[{self.name.title()}] use special skill and heal 150 health! [{target.name.title()}] health now is {target._health}")
    



