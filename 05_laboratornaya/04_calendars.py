number = int(input('Введите элемент последовательности: '))
counter = 0
while number != 0:
    if number % 2 == 0:
        counter = counter + 1
    number = int(input('Введите элемент последовательности: '))
print(counter)