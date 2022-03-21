counter = 0
for i in range(30, 36):
    print('Людей в', i, '-м секторе: ')
    number = int(input())
    if number <= 10:
        print('Все спокойно.')
    else:
        print('Нарушение! Слишком много людей в секторе!')
        counter += 1
print('\nКоличество нарушений:', counter)