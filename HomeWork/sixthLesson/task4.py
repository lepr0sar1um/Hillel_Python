import random as r
import string

letters = string.ascii_lowercase
random_str = ''.join(r.choice(letters) for i in range(r.randint(1, 33)))
my_string_list = [random_str[i:i + r.randint(3, 5)] for i in range(0, len(random_str), r.randint(4, 10))]
my_int_list = r.sample(range(0, 200), r.randint(4, 10))
my_mixed_list = my_string_list + my_int_list
my_final_list = [value for value in my_mixed_list if type(value) == str]

print(my_final_list)