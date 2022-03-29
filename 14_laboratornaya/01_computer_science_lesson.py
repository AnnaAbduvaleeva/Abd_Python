x = input('Введите положительное число: ')
k = 0
if x.replace('.', '').isdigit():
    x = float(x)
    num = x
    if num <= 0:
        print('Введенное число не является положительным.')
    else:
        if num >= 1:
            while num // 10 >= 1:
                num = num // 10
                k += 1
            print(x/10**k, ' * 10**', k, sep='')
        else:
            while num < 1:
                k += 1
                num = num * 10
            print("%.3f" % num, ' * 10**-', k, sep='')
else:
    print('Вы ввели не число.')