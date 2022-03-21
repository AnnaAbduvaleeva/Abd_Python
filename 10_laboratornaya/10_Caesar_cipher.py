text = list(input('Введите сообщение: '))
k = int(input('Введите сдвиг: '))
ABC = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
       'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

index = 0
for i in range(len(text)):
    flag = 0
    for j in range(33):
        if text[i] == ABC[j]:
            index = j
            flag = 1
    if flag == 1:
        text[i] = ABC[(index + k) % 33]

encrypted_message = ''
for i in range(len(text)):
    encrypted_message += str(text[i])
print('Зашифрованное сообщение:', encrypted_message)