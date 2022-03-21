v = int(input('Укажите скорость: '))
t = int(input('Укажите время: '))
s = v * t
print(s - (s // 115) * 115)
