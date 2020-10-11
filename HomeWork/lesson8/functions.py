import random
import string


def read_domains(path: str) -> list:
    file = open(path, "r")
    return [line.replace(".", "").strip() for line in file]


def read_names(path: str) -> list:
    file = open(path, "r")
    return [line.strip().split("\t")[1] for line in file]


def create_email(names: list, domains: list):
    name = random.choice(names)
    domain = random.choice(domains)
    number = random.randint(100, 999)
    domain_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 7)))
    print(name + "." + str(number) + "@" + domain_str + "." + domain)
