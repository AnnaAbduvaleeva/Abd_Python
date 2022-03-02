X = int(input('Введите сумму вклада: '))
Y = int(input('Введите сумму, которую хотите достичь: '))
P = float(input('Введите процентную ставку: '))
years = 0
while X < Y:
    X = int(X + X * P * 0.01)
    years = years + 1
print(years)