print('Начался 8-часовой рабочий день')
hours = 1
tasks = 0
calls = 0
while hours <= 8:
    print(hours, '- й час')
    tasks = int(input('Сколько задач решит Максим? ')) + tasks
    k = int(input('Звонит жена. Взять трубку? (1 - да, 0 - нет) '))
    if k == 1:
        calls = calls + 1
    hours = hours + 1
print('\nРабочий день закончился. Всего выполнено задач:', tasks)
if calls > 0:
    print('Нужно зайти в магазин.')