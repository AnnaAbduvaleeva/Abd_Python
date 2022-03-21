x = int(input('Введите х: '))
res = 1
for i in range(1, 6, 1):
    res *= (x - (2 ** i - 1)) / (x - (2 ** i))
print(res)
