a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
c = int(input('Введите число с: '))
s = 0
n = 0
for i in range(a, b + 1):
    if i % c == 0:
        s += i
        n += 1
print('Среднее арифметическое:', s / n)