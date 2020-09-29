import random

list_len = random.randint(0, 10)
my_list = random.sample(range(0, 200), list_len)
print("Generated list of values: ", my_list, "\nIts len is: ", len(my_list))
my_indexes = [x for x in range(list_len)]
print("Generated ist of indexes: ",my_indexes)
for index in my_indexes:
    print(my_list[index])