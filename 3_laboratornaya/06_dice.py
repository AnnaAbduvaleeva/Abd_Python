a = int(input('Кубик Кости: '))
b = int(input('Кубик владельца: '))
if a > b:
    print('Разность:', a-b)
    print('Костя платит', (a-b)*1000, 'долларов')
    print('Игра окончена')
elif a == b:
    print('Разность:', a - b)
    print('Никто не платит')
    print('Игра окончена')
else:
    print('Сумма', a+b)
    print('Владелец платит', (a+b)*1000, 'долларов')
    print('Игра окончена')