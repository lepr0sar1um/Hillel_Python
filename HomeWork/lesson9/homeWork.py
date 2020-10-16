import Hillel_Python.HomeWork.lesson9.functions as f

path = "/Users/ivanyeremenko/PycharmProjects/Hillel/Hillel_Python/HomeWork/authors.txt"

authors = f.read_file(path)
dates = f.find_dates(authors)
full_date = f.join_dates(dates)
