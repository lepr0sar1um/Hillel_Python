import calendar

month = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
         "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
var = input("Enter the name or number of the month: ")
if var.isdigit():
    if int(var) in month.values():
        print(calendar.monthrange(2020, int(var))[1])
elif var.capitalize() in month:
    print(calendar.monthrange(2020, month[var.capitalize()])[1])
else:
    print("!")
