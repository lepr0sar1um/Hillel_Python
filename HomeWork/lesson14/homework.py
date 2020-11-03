import sys
from typing import Final

import Hillel_Python.HomeWork.lesson14.Units as U

MAGIC_TYPE: Final = {
    'f': 'Fire',
    'a': 'Air',
    'w': 'Water'
}

BOW_TYPE: Final = {
    'b': 'Bow',
    'cb': 'Crossbow'
}

WEAPON_TYPE: Final = {
    's': 'Sword',
    'a': 'Axe',
    'p': 'Peak'
}

mage = U.Mage('John', 'SunShine', magic=MAGIC_TYPE['f'])
archer = U.Archer('Jack', 'MoonShine', bow_type=BOW_TYPE['cb'])
knight = U.Knight('John', 'RiverFrost', weapon_type=WEAPON_TYPE['a'])

sys.stdout = open('output.txt', 'w')

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

sys.stdout.close()