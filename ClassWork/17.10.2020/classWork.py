# import json
#
# my_dict = {"name": "John", "info": {"age": 30, "sex": "male"}}
# write = {"name": "John", "info": {"age": 30, "sex": "male", "zip_code": 123123}}
#
# ###
# # my_json = json.dumps(my_dict)  # convert dict to string
# # print(my_json, type(my_json))
# ###
#
# ###
# # my_json = json.dumps(my_dict, indent=4)  # indent = string formatting (gaps)
# # print(my_json)
# ###
#
# ###
# # my_dict_2 = json.loads(my_json)  # convert string to dict
# # print(my_dict_2, type(my_dict_2))
# ###
#
# ###
# file = "test.json"
# new_file = "new_json.json"
#
# with open(file, "r") as json_file:
#     # data = json_file.read()
#     data = json.load(json_file)  # load = load object (without converting to string)
#     print(data, type(data))
#
# with open(new_file, "w") as new_file:
#     json.dump(write, new_file, indent=2)
#
#
#


import csv

data = []
with open("text.csv", "r") as file:
    csvreader = csv.reader(file, delimiter=",")
    for row in csvreader:
        # print(row)
        data.append(row)
header = data.pop(0)


with open("text_new.csv", "w") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerow(data)
    csvwriter.writerow([10, 20])
