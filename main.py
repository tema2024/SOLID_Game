from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Классы бойца и монстра
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        return self.weapon.attack()

class Monster:
    # Монстр может иметь различные характеристики, здесь для простоты оставлено пустым
    pass

# Демонстрация боя
def battle_demo():
    # Создание оружия
    sword = Sword()
    bow = Bow()

    # Создание бойца с мечом
    fighter = Fighter(sword)
    print("Боец выбирает меч.")
    print(fighter.fight())
    print("Монстр побежден!\n")

    # Смена оружия на лук
    fighter.changeWeapon(bow)
    print("Боец выбирает лук.")
    print(fighter.fight())
    print("Монстр побежден!")

battle_demo()
