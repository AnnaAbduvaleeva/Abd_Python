a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a == b == c:
    print('3')
elif a == b or a == c:
    print('2')
elif a != b != c:
    print('0')