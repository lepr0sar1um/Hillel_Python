import json
import re


json_file = "data.json"


def by_text_length(tmp_dict):
    return len(tmp_dict['text'])


def by_death_date(tmp_dict):
    pass


def by_second_name(tmp_dict):
    pass


def read_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def sort_by_second_name(data):
    data = re.sub(r'c. ', data['years'])



def sort_by_death_date(data):
    pass


def sort_by_text_length(data):
    sorted_dict = sorted(data, key=by_text_length, reverse=True)
    return sorted_dict


data = read_file(json_file)
print(sort_by_text_length(data))