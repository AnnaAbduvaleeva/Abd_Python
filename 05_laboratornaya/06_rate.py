number = int(input('Введите число: '))
num_of_negative = 0
num_of_positive = 0
while number != 0:
    if number < 0:
        num_of_negative = num_of_negative + 1
    else:
        num_of_positive = num_of_positive + 1
    number = int(input('Введите число: '))
print('Количество положительных чисел:', num_of_positive)
print('Количество отрицательных чисел:', num_of_negative)