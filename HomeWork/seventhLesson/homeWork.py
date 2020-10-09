from Hillel_Python.HomeWork.seventhLesson import backyard as make

my_list = make.random_list(20, 1, 100)
make.my_print(my_list)

my_dict = {key: make.random_tuple() for key in ('a', 'b', 'c')}
make.my_print(my_dict)

my_dict_1 = make.random_dict()
my_dict_2 = make.random_dict()

var1 = make.list_of_similar_keys(my_dict_1, my_dict_2)
make.my_print(var1)

var2 = make.list_of_different_keys(my_dict_1, my_dict_2)
make.my_print(var2)

var3 = make.new_dict_of_key_and_value(my_dict_1, my_dict_2)
make.my_print(var3)

var4 = make.joined_dict(my_dict_1, my_dict_2)
make.my_print(var4)

