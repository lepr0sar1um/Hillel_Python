my_str = "My long string"
l_limit = 'o'
r_limit = 'g'

l_limit_index = my_str.find(l_limit)
r_limit_index = my_str.rfind(r_limit)
sub_str = my_str[l_limit_index+1:r_limit_index]
print(sub_str)