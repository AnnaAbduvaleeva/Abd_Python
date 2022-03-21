import random

N = int(input('Введите количество человек в классе: '))
count_3 = 0
count_4 = 0
count_5 = 0
for i in range(1, N+1):
    grade = random.randint(3, 5)
    if grade == 3:
        count_3 += 1
    elif grade == 4:
        count_4 += 1
    else:
        count_5 += 1
print('Сегодняшние оценки\n5:', count_5, '\n4:', count_4, '\n3:', count_3)
if count_3 > count_4 and count_3 > count_5:
    print('Сегодня больше троечников.')
elif count_4 > count_3 and count_4 > count_5:
    print('Сегодня больше хорошистов.')
else:
    print('Сегодня больше отличников.')
