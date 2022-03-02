salary = int(input('Введите вашу зарплату: '))
if salary < 10000:
    tax = salary / 100 * 13
elif salary <= 50000:
    tax = (salary - 10000) * 0.2 + 10000 * 0.13
elif salary <= 100000:
    tax = (salary - 50000) * 0.3 + (50000 - 10000) * 0.2 + 10000 * 0.13
print('Налог составляет', tax, 'рублей')