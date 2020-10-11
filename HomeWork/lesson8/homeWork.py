import Hillel_Python.HomeWork.lesson8.functions as f

names = "/Users/ivanyeremenko/PycharmProjects/Hillel/Hillel_Python/HomeWork/names.txt"
domains = "/Users/ivanyeremenko/PycharmProjects/Hillel/Hillel_Python/HomeWork/domains.txt"

domains_list = f.read_domains(domains)
names_list = f.read_names(names)
email = f.create_email(names_list, domains_list)
