import random

list_len = random.randint(1, 10)
my_list = random.sample(range(0, 200), list_len)
first, *other = my_list
new_list = [*other, first]
