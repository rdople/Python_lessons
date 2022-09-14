# За допомогою ООП створи дві армії. В кожній кілька класів юнитів:
# Маг, Лучник, Лицар, додай ще за бажанням. Юнити мають як загальні якості, наприклад рівень здоров'я,
# так і класові, наприклад діапазон рівеня атаки, тип атаки, тип броні
# Кожна армія по черзі наносить атаку юніту ворожої армії, або лікує юніта своєї армію,
# в залежності від класу юніта (наприклад, маг може атакувати або лікувати)
# За бажанням, додай випадковості, наприклад
#     Атака з діапазону рівня атаки класу
#     Лікування з діапазону рівня лікування
#     Вибір між лікуванням або атакою
#     Частка урону яку поглинає броня
#     Можливість критичного удару
# Так почнеться битва!
#
from random import randint


class Warrior:
    unit_type: str
    warrior_name: str
    warrior_classification: str
    damage: int = 0
    health: int = 0
    defence: int = 0
    population: int = 0

    def __init__(self, warrior_name: str, warrior_classification: str, unit_type: str, damage: int,
                 health: int, defence: int, population: int):
        self.unit_type: str = unit_type
        self.warrior_name: str = warrior_name
        self.warrior_classification: str = warrior_classification
        self.damage: int = damage
        self.health: int = health
        self.defence: int = defence
        self.population: int = population

    def self_medication(self):
        healing = randint(0, 5)
        self.health += healing
        if healing != 0:
            print(f"The {self.warrior_name} has got some medics + {healing} and total health = {self.health}")
        else:
            None
        return self.health

    def get_population(self) -> int:
        return self.population

    def defeated_warrior(self) -> None:
        self.population -= 1
        print(f"Another good man dies young")


# class Army:
#     race_type: str
#     total_damage: int
#     total_health: int
#     total_defence: int
#     total_population: int
#
#     def __init__(self, unit_type: str, damage: int,
#                  health: int, defence: int, population: int):
#         self.unit_type: str = unit_type
#         self.damage: int = damage
#         self.health: int = health
#         self.defence: int = defence
#         self.population: int = population
#
#

def total_data_army(warrior_1, warrior_2):
    total_damage = (warrior_1.damage * warrior_1.population) + (warrior_2.damage * warrior_2.population)
    total_health = (warrior_1.health * warrior_1.population) + (warrior_2.health * warrior_2.population)
    total_defence = (warrior_1.defence * warrior_1.population) + (warrior_2.defence * warrior_2.population)
    total_population = warrior_1.population + warrior_2.population
    print(f"{warrior_1.unit_type} army total info:")
    print(f"{total_damage=}")
    print(f"{total_health=}")
    print(f"{total_defence=}")
    print(f"{total_population=}\n")
    return total_health, total_defence, total_population, total_damage


knight = Warrior(warrior_name='knight', warrior_classification='infantry', unit_type='human', damage=randint(7, 10),
                 health=35, defence=12, population=4)

archer = Warrior(warrior_name='archer', warrior_classification='shooter', unit_type='human', damage=randint(10, 12),
                 health=30, defence=10, population=6)

vampire = Warrior(warrior_name='vampire', warrior_classification='infantry', unit_type='undead', damage=randint(5, 8),
                  health=40, defence=10, population=4)

warlock = Warrior(warrior_name='warlock', warrior_classification='shooter', unit_type='undead', damage=randint(11, 15),
                  health=40, defence=10, population=6)

knight.self_medication()
archer.self_medication()
print(f"{knight.damage=}")
print(f"{archer.damage=}\n")

total_data_army(knight, archer)
total_data_army(vampire, warlock)


def battle(humans, undeads):
     while humans.population
