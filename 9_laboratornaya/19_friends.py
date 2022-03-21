N = int(input('Кол-во друзей: '))
K = int(input('Долговых расписок: '))
print()
debt_list = [0 for i in range(N)]
for i in range(K):
    print(i + 1, 'расписка')
    debtor = int(input('Кому: '))
    creditor = int(input('От кого: '))
    summa = int(input('Сколько: '))
    print()
    debt_list[debtor - 1] -= summa
    debt_list[creditor - 1] += summa
print('Баланс друзей:')
for i in range(N):
    print(i + 1, ':', debt_list[i])