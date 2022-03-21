len_title = int(input('Введите общую длину колонтитула в символах: '))
num_exclam_marks = int(input('Введите желаемое количество восклицательных знаков: '))
title = ''
for i in range((len_title - num_exclam_marks) // 2):
    title += '~'
for i in range(num_exclam_marks):
    title += '!'
for i in range((len_title - num_exclam_marks) // 2):
    title += '~'
print(title)