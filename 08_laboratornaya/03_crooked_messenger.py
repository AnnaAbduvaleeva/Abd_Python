lst = input('Введите текст: ')
for i in range(len(lst)):
    if lst[i] == '*':
        print('Символ ‘*’ стоит на позиции', i + 1)