x = 8
y = 10
print('Марсоход находится на позиции', x, y, 'введите команду:')
command = input()
flag = 1
while flag != 0:
    if command == 'W':
        if y + 1 <= 20:
            y += 1
        else:
            print('Марсоход уперся в стену.')
    if command == 'S':
        if y - 1 >= 0:
            y -= 1
        else:
            print('Марсоход уперся в стену.')
    if command == 'A':
        if x - 1 >= 0:
            x -= 1
        else:
            print('Марсоход уперся в стену.')
    if command == 'D':
        if x + 1 <= 15:
            x += 1
        else:
            print('Марсоход уперся в стену.')
    if command == 'Stop':
        flag = 0
    else:
        print('Марсоход находится на позиции', x, y, 'введите команду:')
        command = input()