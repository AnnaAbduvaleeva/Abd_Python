num = int(input('Введите четырехзначное число: '))
a = num % 10
b = (num % 100) // 10
c = (num // 100) % 10
d = num // 1000
print(d, c, b, a)