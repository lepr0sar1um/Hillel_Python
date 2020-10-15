import Hillel_Python.HomeWork.lesson9.functions as f

path = "/Users/ivanyeremenko/PycharmProjects/Hillel/Hillel_Python/HomeWork/authors.txt"

authors = f.read_file(path)
dates = f.find_date(authors)
# print(authors)
# print("\n".join(dates))

print(f.create_dict(dates))
