my_str = input('Введите строку (h должно встречаться минимум 2 раза: ')
finish_index = 0
start_index = 0
for i in range(len(my_str)):
    if my_str[i] == 'h':
        finish_index = i
for i in range(len(my_str)-1, -1, -1):
    if my_str[i] == 'h':
        start_index = i
print(my_str[finish_index-1:start_index:-1])