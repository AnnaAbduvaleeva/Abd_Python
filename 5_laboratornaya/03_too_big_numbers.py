number = int(input('Введите число: '))
counter = 1
while number > 10:
    number = number // 10
    counter = counter + 1
print('Во введенном числе', counter, 'цифр.')