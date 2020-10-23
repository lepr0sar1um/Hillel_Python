import json

json_file = "data.json"


def by_text_length(tmp_dict):
    return len(tmp_dict['text'])


def by_death_date(tmp_dict):
    # знаю, это стремный костыль, но как сделать умнее я не придумал :(
    death_date = tmp_dict['years'].split('–')[-1].replace('c. ', '').replace('.', '').strip()
    if 'BC' in death_date:
        return -int(death_date.split(' ')[0])
    return int(death_date)


def by_second_name(tmp_dict):
    return tmp_dict['name'].split(' ')[-1]


def read_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def sort_by_second_name(data):
    sorted_dict = sorted(data, key=by_second_name)
    return sorted_dict


def sort_by_death_date(data):
    sorted_dict = sorted(data, key=by_death_date)
    return sorted_dict


def sort_by_text_length(data):
    sorted_dict = sorted(data, key=by_text_length, reverse=True)
    return sorted_dict


data = read_file(json_file)
