import Hillel_Python.HomeWork.lesson14.Units as U

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

mage = U.Mage('John', 'SunShine', magic=MAGIC_TYPE['f'])
archer = U.Archer('Jack', 'MoonShine', bow_type=BOW_TYPE['cb'])
knight = U.Knight('John', 'RiverFrost', weapon_type=WEAPON_TYPE['a'])

print(mage)
print(archer)
print(knight)

print('------------')

mage.health = 98
archer.health = 71
knight.health = 90

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
