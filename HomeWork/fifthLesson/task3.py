import random

list_len = random.randint(1, 10)
my_list_1 = random.sample(range(0, 200), list_len)
my_list_2 = random.sample(range(0, 200), list_len)

sorted_list_1 = [element for element in my_list_1 if not element % 2]
sorted_list_2 = [element for element in my_list_2 if element % 2]
my_result = [*sorted_list_1, *sorted_list_2]
