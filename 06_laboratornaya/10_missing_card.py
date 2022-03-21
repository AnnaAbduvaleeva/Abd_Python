N = int(input('Введите число карточек: '))
cards = input('Последовательно введите номера оставшихся карточек (от 1 до N): ').split()
counter = 0
if int(cards[0]) != 1:
    print('Отсутствует карточка с номером', 1)
if int(cards[len(cards) - 1]) != N:
    print('Отсутствует карточка с номером', N)
for i in range(0, len(cards) - 1):
    if int(cards[i]) != (int(cards[i+1]) - 1):
        counter += 1
        print('Отсутствует карточка с номером', counter + 1)
        break
    else:
        counter += 1