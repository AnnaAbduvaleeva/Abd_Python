first_list = input('Введите 3 целых числа: ').split()
second_list = input('Введите 7 целых чисел: ').split()
new_list = list(set(first_list + second_list))
print(new_list)
