a = int(input('Введите левую координату отрезка: '))
b = int(input('Введите правую координату отрезка: '))
counter = 0
my_sum = 0
for i in range(a, b+1):
    if i % 3 == 0:
        counter += 1
        my_sum += i
print('Среднее арифметическое чисел кратных 3:', round(my_sum / counter, 3))