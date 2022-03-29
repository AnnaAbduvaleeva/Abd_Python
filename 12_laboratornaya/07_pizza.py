N = int(input('Введите кол-во заказов: '))
orders_dict = dict()

for i in range(N):
    print(i + 1, 'заказ: ', end='')
    order = input().split()

    name = order[0]
    pizza = order[1]
    num = int(order[2])

    if name not in orders_dict:
        orders_dict[name] = {pizza: num}
    else:
        if pizza not in orders_dict[name]:
            orders_dict[name][pizza] = num
        else:
            orders_dict[name][pizza] += num

for fam, elem in sorted(orders_dict.items()):
    print(fam, ':')
    for name_pizza in elem.keys():

        print('\t', name_pizza, ':', elem[name_pizza])