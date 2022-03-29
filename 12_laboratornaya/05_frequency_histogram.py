text = input('Введите текст: ')
original_dict = dict()

for elem in text:
    if elem in original_dict:
        original_dict[elem] += 1
    else:
        original_dict[elem] = 1
print('Оригинальный словарь частот:')
for key in sorted(original_dict):
    print(key, ':', original_dict[key])

invert_dict = dict()
for symbol in original_dict:
    if original_dict[symbol] in invert_dict:
        invert_dict[original_dict[symbol]].append(symbol)
    else:
        invert_dict[original_dict[symbol]] = [symbol]
print('Инвертированный словарь частот:')
for key in sorted(invert_dict):
    print(key, ':', invert_dict[key])