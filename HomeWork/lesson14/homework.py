from contextlib import redirect_stdout
from Hillel_Python.HomeWork.lesson14.Units import Mage, Archer, Knight

MAGIC_TYPE = {
    'f': 'Fire',
    'a': 'Air',
    'w': 'Water'
}

BOW_TYPE = {
    'b': 'Bow',
    'cb': 'Crossbow'
}

WEAPON_TYPE = {
    's': 'Sword',
    'a': 'Axe',
    'p': 'Peak'
}

mage = Mage('John', 'SunShine', magic=MAGIC_TYPE['f'])
archer = Archer('Jack', 'MoonShine', bow_type=BOW_TYPE['cb'])
knight = Knight('John', 'RiverFrost', weapon_type=WEAPON_TYPE['a'])

with open('output.txt', 'w') as f:
    with redirect_stdout(f):
        print(pow)

print(mage)
print(archer)
print(knight)

print('------------')

mage.health = 88
archer.health = 91
knight.health = 9

mage.heal()
archer.heal()
knight.heal()

mage.increase_stat()
archer.increase_stat()
knight.increase_stat()

print('------------')

print(mage)
print(archer)
print(knight)
