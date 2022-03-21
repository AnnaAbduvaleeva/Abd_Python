N = int(input('Введите длину списка: '))
res_list = [1 if i % 2 == 0 else i % 5 for i in range(N)]
print(res_list)