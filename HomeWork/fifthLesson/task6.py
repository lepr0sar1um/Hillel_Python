my_string = "43 больше чем 34 но меньше чем 56"
total = sum(int(word) for word in my_string.split(' ') if word.isnumeric())
print(total)
