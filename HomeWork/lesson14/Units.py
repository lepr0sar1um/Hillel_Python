class Unit:
    def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
                 intellect: int = 1):
        self.__name = name
        self.__clan = clan
        self.__health = health
        self.__strength = strength
        self.__dexterity = dexterity
        self.__intellect = intellect

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def clan(self):
        return self.__clan

    @clan.setter
    def clan(self, clan):
        self.__clan = clan

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength):
        self.__strength = strength

    @property
    def dexterity(self):
        return self.__dexterity

    @dexterity.setter
    def dexterity(self, dexterity):
        self.__dexterity = dexterity

    @property
    def intellect(self):
        return self.__intellect

    @intellect.setter
    def intellect(self, intellect):
        self.__intellect = intellect

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
        self.__magic = magic

    def __repr__(self):
        return f"I am {self.name}, and I am a {self.magic} Mage. I have such stats: \nClan - {self.clan}" \
               f"\nHealth = {self.health}, \nStrength = {self.strength}, \nDexterity = {self.dexterity}, " \
               f"\nIntellect = {self.intellect} "

    @property
    def magic(self):
        return self.__magic

    @magic.setter
    def magic(self, magic):
        self.__magic = magic

    def increase_stat(self):
        stat = 10 - self.intellect
        increase = 1 if stat >= 1 else stat
        self.intellect += increase
        return self.intellect


class Archer(Unit):
    def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
                 intellect: int = 1, bow_type=''):
        super().__init__(name, clan, health, strength, dexterity, intellect)
        self.__bow_type = bow_type

    def __repr__(self):
        return f"I am {self.name}, and I am a {self.bow_type} Archer. I have such stats: \nClan - {self.clan}" \
               f"\nHealth = {self.health}, \nStrength = {self.strength}, \nDexterity = {self.dexterity}, " \
               f"\nIntellect = {self.intellect} "

    @property
    def bow_type(self):
        return self.__bow_type

    @bow_type.setter
    def bow_type(self, bow_type):
        self.__bow_type = bow_type

    def increase_stat(self):
        stat = 10 - self.dexterity
        increase = 1 if stat >= 1 else stat
        self.dexterity += increase
        return self.dexterity


class Knight(Unit):
    def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
                 intellect: int = 1, weapon_type=''):
        super().__init__(name, clan, health, strength, dexterity, intellect)
        self.__weapon_type = weapon_type

    def __repr__(self):
        return f"I am {self.name}, and I am a {self.weapon_type} Knight. I have such stats: \nClan - {self.clan}" \
               f"\nHealth = {self.health}, \nStrength = {self.strength}, \nDexterity = {self.dexterity}, " \
               f"\nIntellect = {self.intellect} "

    @property
    def weapon_type(self):
        return self.__weapon_type

    @weapon_type.setter
    def weapon_type(self, weapon_type):
        self.__weapon_type = weapon_type

    def increase_stat(self):
        stat = 10 - self.strength
        increase = 1 if stat >= 1 else stat
        self.strength += increase
        return stat
