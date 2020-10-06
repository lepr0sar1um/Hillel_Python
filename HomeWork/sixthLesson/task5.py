import random
import string

letters = string.ascii_lowercase
random_str = ''.join(random.choice(letters) for i in range(random.randint(1, 33)))
new_list = [*set(random_str)]
print(new_list)