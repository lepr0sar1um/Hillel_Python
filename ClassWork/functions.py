from random import randint


def get_rand(mask):
    if len(mask) == 1:
        return randint(0, 9)
    if len(mask) == 2:
        return randint(0, 99)
    if len(mask) == 3:
        return randint(0, 255)


def get_ip(mask):
    ip_parts = [str(get_rand(mask[i])) for i in range(4)]
    return ".".join(ip_parts)


def sort_ip_key(ip):
    return [int(part) for part in ip.split(".")]


def generate_list_of_ip_addresses(number: int, mask="xxx.xxx.xxx.xxx", repeat=True, sort=False) -> list:
    mask = mask.split(".")
    ip_list = []
    for _ in range(number):
        ip_list.append(get_ip(mask))
    if not repeat:
        ip_list = list(set(ip_list))
    if sort:
        ip_list.sort(key=sort_ip_key)
    return ip_list
