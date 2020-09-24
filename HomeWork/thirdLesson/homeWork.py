separator = "\n#####################################################\n"
value = int(input("Input some integer: "))
new_value = value / 2 if value < 100 else - value
print(new_value, separator)

new_value = 1 if value < 100 else 0
print(new_value, separator)

new_value = True if value < 100 else False
print(new_value, separator)

my_str = input("Please, input some string: ")
print(my_str.upper(), separator)

print(my_str.lower(), separator)

my_str = my_str * 2 if len(my_str) < 5 else my_str
print(my_str, separator)
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)
for symbol in my_str:
    if symbol.isdigit() or symbol.isalpha():
        print(symbol)
print(separator)

for symbol in my_str:
    if not (symbol.isdigit() or symbol.isalpha()):
        print(symbol)
print(separator)

for symbol in my_str:
    if not (symbol.isdigit() or symbol.isalpha() and " "):
        print(symbol)
print(separator)
