value = input("Please, enter the fractional number: ")
if "." not in value:
    print("Incorrect input! Please, enter fractional numbers only and use a dot as a separator.")
else:
    try:
        value = float(value)
        print(value ** -1)
    except ValueError:
        print("Incorrect input! Please, enter digits only.")