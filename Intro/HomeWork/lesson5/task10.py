import random

list_len = random.randint(5, 15)
my_list = random.sample(range(15), list_len)
list_of_elements = [my_list[i] for i in range(1, list_len - 1)
                    if my_list[i] > (my_list[i - 1] + my_list[i + 1])]
print(list_of_elements, len(list_of_elements))
