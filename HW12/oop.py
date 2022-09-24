from random import randint


class Warrior:

    def __init__(self):
        self.type = 'Нalberdier'
        self.health = 10
        # self.defence = randint(3, 5)
        # self.attack = randint(2, 3)
        self.defence = 3
        self.attack = 6

    @property
    def is_not_defeated(self) -> bool:
        if self.health <= 0:
            print(f"Another good man {self.type}  dies young ")
        return self.health > 0

    def self_medication(self):
        if self.health <= 0:
            print(f"This {self.type} fighter tried to heal, but nothing will help him. Sad story((\n")
        if self.health > 15:
            pass
        else:
            healing = randint(0, 3)
            self.health += healing
            if healing != 0:
                print(f"{self.type} has got some medics + {healing} and total health = {self.health}\n")

        return self.health


class Skeleton(Warrior):

    def __init__(self):
        super().__init__()
        self.type = 'Skeleton'
        self.health = 10
        # self.defence = randint(4, 6)
        # self.attack = randint(1, 3)
        self.defence = 3
        self.attack = 6


def fight(unit_1, unit_2) -> bool:
    while unit_1.is_not_defeated and unit_2.is_not_defeated:
        unit_2.health -= (unit_1.attack - unit_2.defence)
        unit_1_real_damage = (unit_1.attack - unit_2.defence)
        print(f"Our hero {unit_1.type} attacks {unit_2.type} with {unit_1.attack} damage points.\n"
              f"Enemy's armor absorbed {unit_2.defence} damage points\n"
              f"So, real damage was: {unit_1_real_damage} points and left him: "
              f"{unit_2.health} points health to enemy\n")
        unit_2.self_medication()

        unit_2_real_damage = (unit_2.attack - unit_2.defence)
        unit_1.health -= (unit_2.attack - unit_1.defence)
        print(f"The enemy {unit_2.type} tries to damage our "
              f"{unit_1.type} with {unit_2.attack} damage points and "
              f"Our armor absorbed {unit_1.defence} damage points\n"
              f"So, real damage was: {unit_2_real_damage} points and left him: "
              f"{unit_2.health} points health to enemy\n") and unit_1.self_medication()\
            if unit_2.is_not_defeated else 0

    return unit_1.is_not_defeated


class Army:

    def __init__(self, name):
        self.list = []
        self.name = name

    def __str__(self):
        return f"from {self.name}\n"

    def add_units(self, unit, amount):
        self.list += [unit() for k in range(amount)]


    @property
    def are_there_warriors(self) -> bool:
        return self.list != []

    @property
    def is_present_warrior(self):
        return self.list[0]

    @property
    def pop(self):
        print(f"{self.name} defeated")
        self.list.pop(0)



class War:
    def fight(self, army_1, army_2) -> bool:
        print(f"Let's start our sacred war!")
        print(f"*********************************************\n")
        while army_1.are_there_warriors and army_2.are_there_warriors:
            if fight(army_1.is_present_warrior, army_2.is_present_warrior):
                army_2.pop
            else:
                army_1.pop
        return army_1.are_there_warriors


humans = Army("Army_of_Humans")
humans.add_units(Warrior, 1)


undeads = Army("Army_of_Undeads")
undeads.add_units(Skeleton, 1)

war = War()
war.fight(humans, undeads)