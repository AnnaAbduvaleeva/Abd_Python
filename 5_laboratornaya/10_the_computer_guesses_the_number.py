hidden_number = int(input('Загадайте число от 0 до 100: '))
low_limit = 0
upper_limit = 100
counter = 1
true = 1
while true:
    N = int((upper_limit + low_limit) / 2)
    print('Твоё число равно, меньше или больше, чем число', N, '? (1 - равно, 2 - больше, 3 - меньше)')
    k = int(input())
    if k == 2:
        low_limit = N
        counter = counter + 1
    elif k == 3:
        upper_limit = N
        counter = counter + 1
    else:
        print('Ваше число:', N)
        print('Число попыток:', counter)
        break

