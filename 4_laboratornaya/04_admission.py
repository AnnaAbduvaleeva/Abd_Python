place = int(input('Введите место в списке поступающих: '))
if place <= 10:
    scores = int(input('Введите количество баллов за экзамены: '))
    if scores >= 290:
        print('Поздравляем, вы поступили!\nБонусом вам будет начисляться стипендия.')
    else:
        print('Поздравляем, вы поступили!\nНо вам не хватило баллов для стипендии.')
else:
    print('К сожалению, вы не поступили.')