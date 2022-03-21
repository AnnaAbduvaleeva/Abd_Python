import random

N = int(input('Введите длину списка: '))
random_lst = [random.randint(-10,10) for i in range(N)]
# print(random_lst)
for elem in random_lst:
    if elem == 0:
        random_lst.remove(elem)
        random_lst.append(elem)
# print(random_lst)
for elem in random_lst[::-1]:
    if elem == 0:
        random_lst.remove(elem)
print(random_lst)