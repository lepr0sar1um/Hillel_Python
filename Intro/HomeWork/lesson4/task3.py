import random

list_len = random.randint(0, 10)
my_list = random.sample(range(0, 200), list_len)
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
else:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)