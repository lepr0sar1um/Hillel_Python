import random
import string

letters = string.ascii_lowercase
random_str_1 = ''.join(random.choice(letters) for i in range(random.randint(1, 33)))
random_str_2 = ''.join(random.choice(letters) for j in range(random.randint(1, 33)))

unique_set_1 = set(random_str_1)
unique_set_2 = set(random_str_2)

my_list = [*set.intersection(unique_set_1, unique_set_2)]
print(my_list)