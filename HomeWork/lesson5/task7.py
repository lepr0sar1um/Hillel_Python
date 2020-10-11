import random
import string

letters = string.ascii_lowercase
random_str = ''.join(random.choice(letters) for i in range(random.randint(1, 33)))
random_str = random_str + '_' if len(random_str) % 2 else random_str
my_list = [random_str[i:i + 2] for i in range(0, len(random_str), 2)]

print(my_list)

