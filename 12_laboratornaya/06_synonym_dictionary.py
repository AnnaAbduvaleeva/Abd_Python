N = int(input('Введите количество пар слов: '))
vocabulary = dict()
for i in range(N):
    print(i + 1, 'пара: ', end='')
    s = input().lower().split(' - ')
    vocabulary[s[0]] = s[1]
    vocabulary[s[1]] = s[0]

word = input('\nВведите слово: ').lower()
while word != 'стоп':
    if word in vocabulary.keys():
        print('Синоним:', vocabulary[word])
    else:
        print('Такого слова в словаре нет.')
    word = input('Введите слово: ').lower()