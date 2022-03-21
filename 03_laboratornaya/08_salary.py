hours = int(input('Введите отработанные часы: '))
balance = int(input('Введите остаток по кредиту: '))
spending = int(input('Введите траты на еду: '))
salary = ((200 * hours) / 2 ** 3) + hours
if salary >= balance + spending:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придется работать!')