n = int(input('Введите натуральное число: '))
S = 1
for i in range(1, n+1, 1):
    S += ((-1) ** i) / (2 ** i)
print(S)