name = input('Введите имя: ')
debt = int(input('Введите сумму долга: '))
print(name, ',ваша задолженность составляет ', debt, ' рублей', sep='')
payment = int(input('Сколько рублей вы внесете прямо сейчас, чтобы её погасить? '))
while payment < debt:
    print('Маловато,', name, '. Давайте ещё раз.')
    payment = int(input('Сколько рублей вы внесете прямо сейчас, чтобы её погасить? '))
print('Отлично,', name, '! Вы погасили долг. Спасибо!')