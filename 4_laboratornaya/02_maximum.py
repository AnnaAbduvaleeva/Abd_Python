a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))
if (a > b) and (a > c):
    print('Максимальное число:', a)
elif (b > a) and (b > c):
    print('Максимальное число:', b)
else:
    print('Максимальное число:', c)