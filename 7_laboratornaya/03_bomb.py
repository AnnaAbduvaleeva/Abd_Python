N = int(input('Введите время до обнуления таймера: '))
for i in range(N, 0, -1):
    print(i, 'секунд до взрыва')
    ans = int(input('Хотите ли вы обезвредить бомбу сейчас? (0 - нет, 1 - да) '))
    if ans == 1:
        print('Бомба обезврежена за', i, 'секунд до взрыва')
        break
else:
    print('Бомба взорвалась.')