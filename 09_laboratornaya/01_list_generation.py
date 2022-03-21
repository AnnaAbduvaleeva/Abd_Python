N = int(input('Введите число: '))
lst = []
for i in range(1, N+1):
    if i % 2 != 0:
        lst.append(i)
print(lst)