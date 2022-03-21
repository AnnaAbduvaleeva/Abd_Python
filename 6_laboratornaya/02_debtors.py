my_str = input('Введите 10 целых чисел: ').split()
number = 0
for i in range(0, len(my_str)):
    if int(my_str[i]) > 0 and int(my_str[i]) % 2 == 0:
        number += 1
print('Из них одновременно являются целыми и четными:', number)
