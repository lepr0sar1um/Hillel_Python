import random
import string

letters = string.ascii_lowercase
random_str = ''.join(random.choice(letters) for i in range(random.randint(1, 33)))
my_list = [random_str[i:i + random.randint(3, 5)] for i in range(0, len(random_str), random.randint(4, 10))]
print(my_list)

new_list = [value[::-1] if index % 2 else value for index, value in enumerate(my_list)]
print(new_list)