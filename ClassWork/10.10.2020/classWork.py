from Hillel_Python import functions

ip_list = functions.generate_list_of_ip_addresses(5, repeat=False, sort=True)
# print(ip_list)


file = open("/Users/ivanyeremenko/file.txt", "r")
print(file.read())
file.close()
