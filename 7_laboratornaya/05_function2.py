a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
c = int(input('Введите шаг: '))
for i in range(b, a - 1, c):
    print('В точке', i, 'функция равна', i**3+2*(i**2)-4*i+1)