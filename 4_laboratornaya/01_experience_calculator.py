points = int(input('Введите количество опыта: '))
if points < 1000:
    print('Ваш уровень: 1')
elif points < 2500:
    print('Ваш уровень: 2')
elif points < 5000:
    print('Ваш уровень: 3')
else:
    print('Ваш уровень: 4')
