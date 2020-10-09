import random
import string

letters = string.ascii_lowercase


def random_list(size, min_range, max_range):
    return random.sample(range(min_range, max_range), size)


def random_tuple():
    return tuple(random.sample(range(-100, 100), 2))


def random_dict():
    return {key: random.randint(1, 100) for key in
            list(''.join(random.choice(letters) for _ in range(random.randint(1, 3))))}


# Return a list of the keys that are in both dictionaries
def list_of_similar_keys(dict_a, dict_b):
    return [key for key in dict_a if key in dict_b]


# Return a list of the keys that are in the dict_a but not in the dict_b dictionary
def list_of_different_keys(dict_a, dict_b):
    return [key for key in dict_a if key not in dict_b]


# Return a new dictionary of {key: value} pairs, for keys that are in the dict_a,
# but not in the dict_b dictionary
def new_dict_of_key_and_value(dict_a, dict_b):
    return {key: value for (key, value) in dict_a.items() if key not in dict_b}


# Combine these two dictionaries into a new dictionary according to the rule:
# if the key is only in one of the two dictionaries, place a {key: value} pair,
# if the key is in two dictionaries, put the pair {key: [value_from_dict_a, value_from_dict_b]}
def joined_dict(dict_a, dict_b):
    return {key: [dict_a.get(key), dict_b.get(key)] if key in dict_a.keys() & dict_b.keys() else dict_a.get(
        key) or dict_b.get(key) for key in
            # will take a couple of values for one key in the intersection of dict_a and dict_b
            # if no intersection will input a couple of key : value from the union of dict_a and dict_b as is
            dict_a.keys() | dict_b.keys()}


def my_print(value):
    return print("*** ", value, " ***")
