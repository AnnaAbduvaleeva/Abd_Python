area = int(input('Введите площадь квартиры (в м2): '))
price = int(input('Введите стоимость квартиры (в млн): '))
if area >= 100:
    if price <= 10:
        print('Квартира подходит.')
    else:
        print('Квартира не подходит.')
elif area >= 80:
    if price <= 7:
        print('Квартира подходит.')
    else:
        print('Квартира не подходит.')
