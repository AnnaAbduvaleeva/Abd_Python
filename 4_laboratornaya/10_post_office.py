time = int(input('Введите время: '))
if 8 <= time < 10 or 12 <= time < 14 or 15 <= time < 18 or 20 <= time < 22:
    print('Можно получить посылку.')
else:
    print('Посылку получить нельзя.')
if 0 <= time < 8 or 10 <= time <= 11 or time == 14 or 18 <= time <= 19 or 22 <= time <= 23:
    print('Посылку получить нельзя.')
else:
    print('Можно получить посылку.')
