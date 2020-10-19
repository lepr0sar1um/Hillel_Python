import Hillel_Python.HomeWork.lesson10.functions as f

my_str = f.random_string()
my_dict = f.random_dict()
my_list = f.random_list(10, 4)

txt_file = "file.txt"
csv_file = "file.csv"
json_file = "file.json"

f.file_writer(txt_file, my_str)
f.file_writer(csv_file, my_list)
f.file_writer(json_file, my_dict)
f.file_writer("file", my_str)
