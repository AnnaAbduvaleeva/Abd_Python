my_str = input('Введите зарплату сотрудника за каждый из 12 месяцев: ').split()
my_sum = 0
for i in range(0, len(my_str)):
    my_sum += float(my_str[i])
print('Средняя зарплата:', round(my_sum / 12, 3))