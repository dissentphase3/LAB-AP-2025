class Human:
    def __init__(self, name, pos_x):
        self.name = name
        try:
            self.__pos_x = int(pos_x)
        except ValueError:
            print('Invalid position!')

    def movement(self, arah):        
        for i in arah:
            if i == 'L':
                self.__pos_x -= self._speed
            elif i == 'R':
                self.__pos_x += self._speed

    def set_speed(self, new_speed):
        self._speed = new_speed

    def get_position(self):
        return self.__pos_x

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self.name

    def set_position(self, new_pos):
        self._position = new_pos

    def get_speed(self):
        return self._speed
    
class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        if self._health <= 0:
            print(f"{self.get_name()} cannot attack, as their health is already 0!")
            return

        if target.get_health() <= 0:
            print(f"{target.get_name()} cannot be attacked, as their health is already 0!")
            return

        target.set_health(target.get_health() - self._power)

        if target.get_health() <= 0:
            target.set_health(0)  # Ensure health doesn't go below 0
            print(f"{target.get_name()} has been defeated!")

    def set_power(self, new_power):
        self._power = new_power

    def get_power(self):
        return self._power

    def set_health(self, new_health):
        self._health = new_health

    def get_health(self):
        return self._health

    def set_armor(self, new_armor):
        self._armor = new_armor

    def get_armor(self):
        return self._armor
    
class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._power = 32
        self._armor = 45
        target.set_health(target.get_health() - self._power)

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self.speed = 4

    def special(self, target):
        self._power = 42
        self.speed = 7
        target.set_health(target.get_health() - self._power)

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self.speed = 4

    def special(self, target):
        self.speed = 6
        target.set_health(target.get_health() + 150)

