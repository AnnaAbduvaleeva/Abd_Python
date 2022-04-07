N = int(input('Кол-во чисел: '))
sequence = []
for i in range(N):
    num = int(input('Число: '))
    sequence.append(num)

print('\nПоследовательность:', end=' ')
for elem in sequence:
    print(elem, end=' ')

number_of_extra_nums = 0
new_sequence = []
change_sequence = new_sequence
reverse_sequence = []
for elem in sequence:
    while reverse_sequence != change_sequence:
        new_sequence.insert(0, elem)
        change_sequence += new_sequence
        reverse_list = list(reversed(change_sequence))
        number_of_extra_nums += 1

if number_of_extra_nums != 0:
    print('\nНужно приписать чисел:', number_of_extra_nums)
    print('Сами числа:', end=' ')



else:
    print('Введенная последовательность симметричная.')