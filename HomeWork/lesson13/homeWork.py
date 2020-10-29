from Hillel_Python.HomeWork.lesson13.FileWriter import FileWriter

data_1 = {1: 1, 2: 2, 3: 3}
data_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_3 = "asdasd asd sd a324 sdf s"

path_1 = 'tmp.json'
path_2 = 'tmp.csv'
path_3 = 'tmp.txt'

# my_writer_1 = FileWriter(path_1, data_1)
# my_writer_2 = FileWriter(path_2, data_2)
# my_writer_3 = FileWriter(path_3, data_3)

my_writer_1 = FileWriter(path_1)
my_writer_2 = FileWriter(path_2)
my_writer_3 = FileWriter(path_3)

my_writer_1.write()
my_writer_2.write()
my_writer_3.write()
