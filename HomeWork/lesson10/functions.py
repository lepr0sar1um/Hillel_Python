import random
import string
import json
import csv


def random_string(min_length=100, max_length=1000, for_dict=False):
    if for_dict:
        return ''.join(random.choice(string.ascii_lowercase) for _ in
                       range(random.randint(max_length, max_length)))
    else:
        return ''.join(random.choice(string.ascii_lowercase + ' ' + ',' + '.' + string.ascii_uppercase) for _ in
                       range(random.randint(min_length, max_length)))


def random_dict():
    return {random_string(min_length=5, max_length=5, for_dict=True): random.randint(-100, 100) for key in range(5, 20)}


def random_list(rows=5, cols=5):
    return [[random.randint(0, 1) for i in range(cols)] for j in range(rows)]


def write_txt(path: str, data):
    with open(path, 'w') as file:
        file.write(data + ("\n" * 9))
    print(f"File '{path}' has successfully been written.")


def write_csv(path: str, data):
    with open(path, 'w') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerows(data)
    print(f"File '{path}' has successfully been written.")


def write_json(path: str, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"File '{path}' has successfully been written.")


def file_writer(path: str, data):
    mode = path.rsplit(".")[-1]
    if mode == "txt":
        write_txt(path, data)
    elif mode == "json":
        write_json(path, data)
    elif mode == "csv":
        write_csv(path, data)
    else:
        raise Exception("Unsupported file format!")
