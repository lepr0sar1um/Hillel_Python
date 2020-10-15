from datetime import datetime
import re


def read_file(path: str) -> list:
    file = open(path, "r")
    return [line.replace("\n", "") for line in file]


def find_date(authors: list) -> list:
    dates = []
    for line in authors:
        if "birthday" in line or "death" in line:
            dates.append(line)
    return dates


def convert_to_date(date_string: str) -> str:
    return str(datetime.strptime(re.sub(r'(\d+)[a-z]+', r'\1', date_string),  '%d %B %Y').strftime('%d/%m/%Y'))


def create_dict(dates: list) -> list:
    return [{"name": line.split("-")[1].split("'")[0].strip(), "date": convert_to_date(line.split("-")[0].strip())} for
            line in dates]
