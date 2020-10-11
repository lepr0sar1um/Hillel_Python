my_str = "My_long str"
l_limit = 'o'
r_limit = 't'

l_limit_index = my_str.find(l_limit)
r_limit_index = my_str.find(r_limit)
sub_str = my_str[l_limit_index+1:r_limit_index]
print(sub_str)