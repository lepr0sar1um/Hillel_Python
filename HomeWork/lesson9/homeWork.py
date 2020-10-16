import os
import Hillel_Python.HomeWork.lesson9.functions as f

path = "/Users/ivanyeremenko/PycharmProjects/Hillel/Hillel_Python/HomeWork/authors.txt"
folder = os.path.abspath(os.curdir)

authors = f.read_file(path)
dates = f.find_dates(authors)
full_date = f.join_dates(dates)


def show_folder(folder="/Users/ivanyeremenko/PycharmProjects/Hillel/Hillel_Python/HomeWork/") -> dict:
    list_dir = sorted(os.listdir(folder))
    files = []
    folders = []

    for item in list_dir:
        path_item = os.path.join(folder, item)
        if os.path.isfile(path_item):
            files.append(path_item)
        else:
            folders.append(path_item)

    files_dict = {"files": files, "folders": folders}

    print(files_dict)


finder = show_folder(folder)
