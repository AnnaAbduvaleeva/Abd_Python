points_rus = int(input('Введите количество баллов по русскому языку: '))
points_math = int(input('Введите количество баллов по математике: '))
points_inf = int(input('Введите количество баллов по информатике: '))
print('\n')
if (points_rus + points_math + points_inf) >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошел на бюджет.')


