menu = input('Доступное меню: ').split(';')
menu_str = ''
for i in range(len(menu)-1):
    menu_str += ''.join(menu[i]) + ', '
menu_str += ''.join(menu[len(menu)-1])
print('На данный момент в меню есть: ' + menu_str)
