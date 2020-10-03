# my_list = [1, 20, 34, 12, -8]
# Элемент с четным индексом возвести в квадрат
# for index in range(len(my_list)):
#     if index % 2 == 0:
#         print(my_list[index] ** 2)
#     else:
#         print(my_list[index])

###
# for index, value in enumerate(my_list):
#     if index % 2 == 0:
#         print(value ** 2)
#     else:
#         print(value)
###

# Вывести элемент списка в степень его индекса
# for index, value in enumerate(my_list):
#     print(value ** index)
###

# В новый список поместить числовые значения из старого списка, учитывая
# что числа могут быть строкой
# my_list = [1, 2, 3, '4', '5', 6, 7, 'qwe', 8, 'qwz', 9, 1, 3]
# new_list = []
# for value in my_list:
#     try:
#         value = int(value)
#         new_list.append(value)
#     except ValueError:
#         pass
# print(new_list)
###

# Множество SET
# Варианты объявления множества
# Приведение типов
# my_set = set(my_list)
# print(my_set)

# my_str = "bla BLA car"
# print(len(set(my_str.lower())))
# Множество хрнаит в себе уникальные значения без дубликатов

my_set_1 = {1, 2, 3, 7}
my_set_2 = {2, 3, 4}

inter = my_set_1.intersection(my_set_2)
# возвращает пересекающиеся результаты из двух множеств
# в данном слуае 2 и 3
print(inter)

# my_set_1.intersection_update(my_set_2)
# обновляет объекты в my_set_1, результат как в предыдщем примере
# print(my_set_1)

# объединение двух множеств и выводит уникальные значения
union = my_set_1.union(my_set_2)
print(union)

# создается новое множество с отличающимися объектами из двух список
#
dif = my_set_1.difference(my_set_2)
print(dif)

# создается новое множество
#
sim_dif = my_set_1.symmetric_difference(my_set_2)
print(sim_dif)