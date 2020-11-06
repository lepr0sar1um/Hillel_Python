import json
import os
from random import randint, choice
from string import ascii_lowercase as letters


def generate_file_name():
    return ''.join(choice(str(randint(0, 9)) + '_') for _ in range(1, 5)) + ''.join(
        choice(letters) for _ in range(1, 3))


def generate_data_for_file(file_name):
    width = randint(0, 400)
    data = {
        "filename": file_name,
        "width": width,
        "objects":
            [
                {
                    f"object{index}": {
                        "class": symbol,
                        "xmin": width / 4 * index,
                        "xmax": width / 4 * (index + 1),

                    }
                    for index, symbol in enumerate(file_name[0:4]) if symbol != '_'
                }
            ]
    }
    crete_file_and_folder(data, file_name)
    return print("!")


def crete_file_and_folder(data, file_name):
    name = 'tmp_folder'
    if not os.path.isdir(name):
        os.mkdir(name)
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    return print("done")


file = generate_file_name()
generate_data_for_file(file)
