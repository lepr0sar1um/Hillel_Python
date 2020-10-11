import random

my_result = []
my_list = random.sample(range(0, 200), 10)
for value in my_list:
    if value > 100:
        my_result.append(value)
if my_result:
    print(my_result)
else:
    print("All list items are greater than 0")