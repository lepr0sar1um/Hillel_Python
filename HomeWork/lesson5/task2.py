import random

value = random.randint(0, 1000000000000000000000)
result = 0
while not value % 10:
    value = value / 10
    result += 1
