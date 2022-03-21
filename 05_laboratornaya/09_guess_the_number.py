hidden_num = int(input('Загадайте число от 0 до 100: '))
num = int(input('Введите число: '))
k = 1
while num != hidden_num:
    if num > hidden_num:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
        k = k + 1
        num = int(input('Введите число: '))
    else:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
        k = k + 1
        num = int(input('Введите число: '))
print('Вы угадали! Число попыток:', k)