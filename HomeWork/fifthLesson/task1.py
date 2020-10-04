import random

value = random.randint(0, 1000000000000000000000)
result = len([i for i in str(value) if i == '0'])
