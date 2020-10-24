from random import randint


class Person:
    planet = 'Earth'  # атрибут класса

    def __init__(self, name, age, sex):
        self.name = name  # атрибут ЭКЗЕМПЛЯРА класса
        self.age = age
        self.sex = sex

    def increase_age(self):
        self.age += 1


person_1 = Person('John', 23, 'male')
person_2 = Person('Megan', 19, 'female')

print(person_1.name, person_1.age, person_1.sex, person_1.planet)
print(person_2.name, person_2.age, person_2.sex, person_2.planet)
# John 23 male Earth
# Megan 19 female Earth

person_1.name = 'Alex'
person_1.planet = 'Mars'

print(person_1.name, person_1.age, person_1.sex, person_1.planet)
# Alex 23 male Mars

person_1.increase_age()
print(person_1.name, person_1.age, person_1.sex, person_1.planet)
# Alex 24 male Mars

# Calls person_1.increase_age for 1 - 10 times
for _ in range(randint(1, 10)):
    person_1.increase_age()

print(f"{person_1.name} is {person_1.age} years")


