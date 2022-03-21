X = int(input('Введите количество мальчиков: '))
Y = int(input('Введите количество девочек: '))
ans = ''
if X > 2 * Y or Y > 2 * X:
    print('Нет решения.')
elif X >= Y:
    n = X - Y
    for i in range(Y - n):
        ans += 'BG'
    for i in range(n):
        ans += 'BGB'
else:
    n = Y - X
    for i in range(X - n):
        ans += 'GB'
    for i in range(n):
        ans += 'GBG'
print(ans)