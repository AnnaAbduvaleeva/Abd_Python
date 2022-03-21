N = int(input('Кол-во человек: '))
K = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', K, 'человек\n')
circle_of_people = [i for i in range(1, N+1)]
reference_point = 0

while len(circle_of_people) > 1:
    print('Текущий круг людей:', circle_of_people)
    print('Начало счёта с номера', circle_of_people[reference_point])
    i = K % N

    if i + reference_point > N:
        i = i + reference_point - N
        print('Выбывает человек под номером', circle_of_people[i - 1], '\n')
        circle_of_people.pop(i - 1)
        reference_point = i - 1
    else:
        print('Выбывает человек под номером', circle_of_people[i + reference_point - 1], '\n')
        circle_of_people.pop(i + reference_point - 1)
        if i != 0:
            reference_point = i + reference_point - 1
        elif reference_point != 0:
            reference_point = reference_point - 1
        if reference_point >= (N - 1):
            reference_point = reference_point - N + 1
    N -= 1

print('Остался человек под номером', circle_of_people[0])
