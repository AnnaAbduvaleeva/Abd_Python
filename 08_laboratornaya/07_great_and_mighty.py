my_str = input('Введите текст: ').split()
my_max = 0
for word in my_str:
    if len(word) > my_max:
        my_max = len(word)
print('Самое длинное слово, букв:', my_max)