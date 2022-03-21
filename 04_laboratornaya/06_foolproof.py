from math import sqrt
a = int(input('Введите число: '))
a = sqrt (a * a)
if a // 100 == 0 and a % 100 > 9:
    print('Число двузначное.')
else:
    print('Число не двузначное.')