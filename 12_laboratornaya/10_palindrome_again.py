my_str = input("Введите строку: ")
vocabulary = dict()

for i in range(len(my_str)):
    if my_str[i] in vocabulary:
        vocabulary[my_str[i]] += 1
    else:
        vocabulary[my_str[i]] = 1

num = 0
for key in vocabulary:
    parity = vocabulary[key] % 2
    num += parity

if num == 0 or num == 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')