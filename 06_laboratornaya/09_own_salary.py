my_str = input('Введите 10 чисел: ').split()
flag = 1
for i in range(0, len(my_str)-1):
    if int(my_str[i+1]) > int(my_str[i]):
        flag *= 1
    else:
        flag *= 0
if flag == 0:
    print('Введенные числа не упорядочены по возрастанию.')
else:
    print('Введенные числа упорядочены по возрастанию.')