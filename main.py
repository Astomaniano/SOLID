from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print('атака мечом')

class Bow(Weapon):
    def attack(self):
        print('выстрел из лука')

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()

class Monster():
    pass

sword = Sword()
bow = Bow()

fighter = Fighter(sword)

monster = Monster()

fighter.attack()
fighter.changeWeapon(bow)
fighter.attack()

