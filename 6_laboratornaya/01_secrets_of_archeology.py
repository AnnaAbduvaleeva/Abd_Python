lst = [114, 12, 14, 10605, 4907, 450]
for number in lst:
    if number % 2 == 0 and number % 3 != 0:
        print('Число', number, 'подходит')
    else:
        print('Число', number, 'не подходит')