minutes = int(input('Введите количество минут: '))
hours = minutes // 60
minutes = minutes - hours * 60
print(hours, 'hours', minutes, 'minutes')