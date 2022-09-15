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
        return self.health

    def get_population(self) -> int:
        return self.population

    def defeated_warrior(self) -> None:
        self.population -= 1
        print(f"Another good man dies young")


class Army:
    unit_type: str
    total_damage: int
    total_health: int
    total_defence: int
    total_population: int
    warrior_1_name: str
    warrior_1_damage: int
    warrior_1_health: int
    warrior_1_defence: int
    warrior_1_population: int
    warrior_2_name: str
    warrior_2_damage: int
    warrior_2_health: int
    warrior_2_defence: int
    warrior_2_population: int

    def __init__(self, unit_type: str, warrior_1_name: str, warrior_1_damage: int, warrior_1_health: int,
                 warrior_1_defence: int, warrior_1_population: int,warrior_2_name: str, warrior_2_damage: int,
                 warrior_2_health: int, warrior_2_defence: int, warrior_2_population: int):
        self.unit_type: str = unit_type
        self.warrior_1_name: str = warrior_1_name
        self.warrior_1_damage: int = warrior_1_damage
        self.warrior_1_health: int = warrior_1_health
        self.warrior_1_defence: int = warrior_1_defence
        self.warrior_1_population: int = warrior_1_population
        self.warrior_2_name: str = warrior_2_name
        self.warrior_2_damage: int = warrior_2_damage
        self.warrior_2_health: int = warrior_2_health
        self.warrior_2_defence: int = warrior_2_defence
        self.warrior_2_population: int = warrior_2_population
        self.get_total_data_army()

    def get_total_data_army(self):
        self.total_damage = \
            (self.warrior_1_damage * self.warrior_1_population) + (self.warrior_2_damage * self.warrior_2_population)
        self.total_health =\
            (self.warrior_1_health * self.warrior_1_population) + (self.warrior_2_health * self.warrior_2_population)
        self.total_defence =\
            (self.warrior_1_defence * self.warrior_1_population) + (self.warrior_2_defence * self.warrior_2_population)
        self.total_population =\
            self.warrior_1_population + self.warrior_2_population
        return self.total_health, self.total_defence, self.total_population, self.total_damage

    def print_total_data_army(self):
        print(f"{self.unit_type} army total info:")
        print(f"{self.total_damage=}")
        print(f"{self.total_health=}")
        print(f"{self.total_defence=}")
        print(f"{self.total_population=}\n")

    def get_population(self) -> int:
        return self.total_population

    def defeated_warrior(self) -> None:
        self.total_population -= 1
        print(f"Another good man dies young")

    def self_medication_1(self):
        healing = randint(0, 5)
        self.warrior_1_health += healing
        if healing != 0:
            print(f"The {self.warrior_1_name} has got some medics + {healing} "
                  f"and total health = {self.warrior_1_health}")
        self.get_total_data_army()
        return self.warrior_1_health

    def self_medication_2(self):
        healing = randint(0, 5)
        self.warrior_2_health += healing
        if healing != 0:
            print(f"The {self.warrior_2_name} has got some medics + {healing} "
                  f"and total health = {self.warrior_2_health}")
        self.get_total_data_army()
        return self.warrior_2_health


knight = Warrior(warrior_name='knight',
                 warrior_classification='infantry',
                 unit_type='human',
                 damage=randint(7, 10),
                 health=35,
                 defence=12,
                 population=4
                 )

archer = Warrior(warrior_name='archer',
                 warrior_classification='shooter',
                 unit_type='human',
                 damage=randint(10, 12),
                 health=30,
                 defence=10,
                 population=6
                 )

vampire = Warrior(warrior_name='vampire',
                  warrior_classification='infantry',
                  unit_type='undead',
                  damage=randint(5, 8),
                  health=40,
                  defence=8,
                  population=4
                  )

warlock = Warrior(warrior_name='warlock',
                  warrior_classification='shooter',
                  unit_type='undead',
                  damage=randint(11, 15),
                  health=40,
                  defence=8,
                  population=6
                  )

humans = Army(knight.unit_type,
              knight.warrior_name,
              knight.damage,
              knight.health,
              knight.defence,
              knight.population,
              archer.warrior_name,
              archer.damage,
              archer.health,
              archer.defence,
              archer.population
              )
undeads = Army(vampire.unit_type,
               vampire.warrior_name,
               vampire.damage,
               vampire.health,
               vampire.defence,
               vampire.population,
               warlock.warrior_name,
               warlock.damage,
               warlock.health,
               warlock.defence,
               warlock.population
               )

# humans.get_total_data_army()
# undeads.get_total_data_army()
# print(f"{humans.get_population()=}")
# print(f"{undeads.get_population()=}")


def battle(army1, army2):
    # while True:
        # army1.get_population() > 0 or army2.get_population() > 0:
        print(f"{army1.get_total_data_army()=}")
        army1.self_medication_1()
        army1.self_medication_2()
        print(f"{army1.get_total_data_army()=}")



#
battle(humans, undeads)


