grand = float(input('Введите стипендию: '))
expenses = float(input('Введите расходы на проживание: '))
s = expenses - grand
for i in range(2, 11, 1):
    expenses = expenses * 1.03
    s += expenses - grand
print('У родителей необходимо попросить', round(s, 3))