N = int(input('Кол-во чисел: '))
sequence = []
for i in range(N):
    num = int(input('Число: '))
    sequence.append(num)
print('\nПоследовательность:', end=' ')
for elem in sequence:
    print(elem, end=' ')
number_of_extra_nums = 0



if number_of_extra_nums != 0:
    print('\nНужно приписать чисел:', number_of_extra_nums)
    print('Сами числа:', end=' ')



else:
    print('Введенная последовательность симметричная.')