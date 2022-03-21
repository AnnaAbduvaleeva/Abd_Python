num_skates = int(input('Кол-во коньков: '))
skate_size_list = []
for i in range(1, num_skates+1):
    print('Размер', i, 'пары:', end=' ')
    skate_size = int(input())
    skate_size_list.append(skate_size)
num_people = int(input('\nКол-во людей: '))
foot_size_list = []
for j in range(1, num_people+1):
    print('Размер ноги', j, 'человека:', end=' ')
    foot_size = int(input())
    foot_size_list.append(foot_size)
# print(skate_size_list, foot_size_list)
skate_size_list.sort()
foot_size_list.sort()
# print(skate_size_list, foot_size_list)
counter = 0
max_people = 0
for elem in skate_size_list:
    if elem >= foot_size_list[counter]:
        max_people += 1
        counter += 1
print(max_people)

