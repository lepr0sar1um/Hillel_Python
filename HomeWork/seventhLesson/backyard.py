import random


def random_list(size, min_range, max_range):
    return random.sample(range(min_range, max_range), size)


def random_tuple():
    return tuple(random.sample(range(-100, 100), 2))


def my_print(value):
    return print("***", value, "***")