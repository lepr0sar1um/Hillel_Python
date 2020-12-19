my_list = [1, 4, -5, 0]
sort_list = sorted(my_list, reverse=True, key=abs)
print(sort_list)

my_list_1 = ["1", "4", "zasd", "-5", "!0", "qwe", "zxc"]
sort_list_1 = sorted(my_list_1)
print(sort_list_1)


def sort_key(tmp_dict):
    for key in tmp_dict:
        return key


my_list_dict = [
    {1945: "Окончание ВОВ"},
    {1991: "Независимость Украины"},
    {998: "Крещение Руси"}
]

sort_list_dict = sorted(my_list_dict, key=sort_key)
print(sort_list_dict)