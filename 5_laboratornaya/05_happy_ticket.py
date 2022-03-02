number = int(input('Введите шестизначный номер билета: '))
sum1 = number % 10 + (number % 100) // 10 + (number % 1000) // 100
sum2 = number // 100000 + (number // 10000) % 10 + (number // 1000) % 10
if sum1 == sum2:
    print('Ваш билет счастливый!')
else:
    print('К сожалению, ваш билет не счачтливый.')