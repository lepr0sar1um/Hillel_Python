# task 7
my_string = '0123456789'
my_list = []
for i in my_string:
    for j in my_string:
        var = i + j
        my_list.append(int(var))
        my_list.sort()
print(my_list)