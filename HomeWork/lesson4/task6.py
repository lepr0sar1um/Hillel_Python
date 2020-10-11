# task 6
import random

list_len = random.randint(0, 10)
my_list_1 = random.sample(range(0, 200), list_len)
my_list_2 = random.sample(range(0, 200), list_len)
print("Generated list of values: ", my_list_1, "\nIts len is: ", len(my_list_1))
print("Generated list of values: ", my_list_2, "\nIts len is: ", len(my_list_2))
my_indexes = [x for x in range(list_len)]
print(my_indexes)
for index in my_indexes:
    print((my_list_1[index], my_list_2[index]))