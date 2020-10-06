import random
import string

letters = string.ascii_lowercase
random_str_1 = ''.join(random.choice(letters) for i in range(random.randint(1, 33)))
random_str_2 = ''.join(random.choice(letters) for j in range(random.randint(1, 33)))

set_1 = {char for char in random_str_1 if random_str_1.count(char) == 1}
set_2 = {char for char in random_str_2 if random_str_2.count(char) == 1}

my_list = [*set.intersection(set_1, set_2)]
print(my_list)