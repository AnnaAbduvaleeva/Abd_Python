num = int(input('Введите целое число: '))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print('Факториал числа', num, 'равен', factorial)