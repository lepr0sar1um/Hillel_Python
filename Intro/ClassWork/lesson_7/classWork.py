from Hillel_Python.ClassWork import functions

number = 5
mask = "x.x.x.x"
ip_list = functions.generate_list_of_ip_addresses(number, mask, repeat=False, sort=True)
print(ip_list)