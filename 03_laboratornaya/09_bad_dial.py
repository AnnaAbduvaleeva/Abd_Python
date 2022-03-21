mileage = int(input('Введите пробег: '))
date = int(input('Введите сегодняшнее число: '))
sum = mileage // 100 + mileage // 10 % 10 + mileage % 10
if sum > date:
    print('Сброс.')
    print('Пробег: 0')
else:
    print('Сегодня не сломался.')
    print('Пробег:', mileage)