rows = int(input('Введите кол-во рядов: '))
seat = int(input('Введите кол-во сидений в ряде: '))
meter = int(input('Введите кол-во метров между рядами: '))
print('\nСцена\n')
layout = ''
for i in range(seat):
    layout += '='
layout += ' '
for i in range(meter):
    layout += '*'
layout += ' '
for i in range(seat):
    layout += '='
for i in range(rows):
    print(layout)