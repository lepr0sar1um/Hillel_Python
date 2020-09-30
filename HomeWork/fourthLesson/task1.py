import random

my_list = random.sample(range(0, 100), 10)
my_list.sort(reverse=True)
if my_list[0] < 100:
    print("All list items are greater than 100")
else:
    for value in my_list:
        if value > 100:
            print(value)