class Unit:
    def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
                 intellect: int = 1):
        self.name = name
        self.clan = clan
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
        self.intellect = intellect

    def __str__(self, ability):
        return f"I am {self.name}, and I am a {ability} {type(self).__name__}. I have such stats: \nClan - {self.clan}" \
               f"\nHealth = {self.health}, \nStrength = {self.strength}, \nDexterity = {self.dexterity}, " \
               f"\nIntellect = {self.intellect} "

    def heal(self):
        health = 100 - self.health
        to_heal = 10 if health >= 10 else health
        self.health += to_heal
        print(f"I have been healed on {to_heal} points!")
        return self.health


class Mage(Unit):
    def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
                 intellect: int = 1, magic=''):
        super().__init__(name, clan, health, strength, dexterity, intellect)
        self.magic = magic

    def __str__(self):
        return super().__str__(self.magic)

    def increase_stat(self):
        self.intellect += 1 if self.intellect < 10 else self.health
        return self.intellect


class Archer(Unit):
    def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
                 intellect: int = 1, bow_type=''):
        super().__init__(name, clan, health, strength, dexterity, intellect)
        self.bow_type = bow_type

    def __str__(self):
        return super().__str__(self.bow_type)

    def increase_stat(self):
        self.dexterity += 1 if self.dexterity < 10 else self.dexterity
        return self.dexterity


class Knight(Unit):
    def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
                 intellect: int = 1, weapon_type=''):
        super().__init__(name, clan, health, strength, dexterity, intellect)
        self.weapon_type = weapon_type

    def __str__(self):
        return super().__str__(self.weapon_type)

    def increase_stat(self):
        self.strength += 1 if self.strength < 10 else self.strength
        return self.strength
