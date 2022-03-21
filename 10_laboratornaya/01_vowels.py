my_str = input('Введите текст: ')
vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
my_vowels = []
for letter in my_str:
    for vowel in vowels_list:
        if letter == vowel:
            my_vowels.append(letter)
print(my_vowels)