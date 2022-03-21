my_str = input('Введите строку: ')
max_len = 0
counter = 0
for letter in my_str:
    if letter == 's':
        counter += 1
    else:
        if counter >= max_len:
            max_len = counter
            counter = 0
if counter > max_len:
    max_len = counter
print(max_len)