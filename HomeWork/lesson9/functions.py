import re
from datetime import datetime


def read_file(path: str) -> list:
    file = open(path, "r")
    return [line.replace("\n", "") for line in file]


def find_dates(authors: list) -> list:
    dates = []
    for line in authors:
        if "birthday" in line or "death" in line:
            dates.append(line)
    return dates


def convert_to_date(date_string: str) -> str:
    return str(datetime.strptime(re.sub(r'(\d+)[a-z]+', r'\1', date_string), '%d %B %Y').strftime('%d/%m/%Y'))


def create_dict(dates: list) -> list:
    return [{"name": line.split("-")[1].split("'")[0].strip(), "date": convert_to_date(line.split("-")[0].strip())} for
            line in dates]


def join_dates(dates: list) -> dict:
    b_date_list = [line for line in dates if "birthday" in line]
    d_date_list = [line for line in dates if "death" in line]

    b_date_dict = {line.split("-")[1].split("'")[0].strip(): convert_to_date(line.split("-")[0].strip())
                   for line in b_date_list}

    d_date_dict = {line.split("-")[1].split("'")[0].strip(): convert_to_date(line.split("-")[0].strip())
                   for line in d_date_list}

    join_date = [{"name": key, "b_date": b_date_dict.get(key), "d_date": d_date_dict.get(key)} for key in
                 b_date_dict.keys() | d_date_dict.keys()]

    print(join_date)
