my_lst = input('Введите слово: ')
inv_lst = my_lst[::-1]    # 1-й способ
# print(my_lst, inv_lst)
inv_lst_2 = "".join(reversed(my_lst))    # 2-й способ
# print(my_lst, inv_lst_2)
inv_lst_3 = "".join([(my_lst[len(my_lst) - i - 1]) for i in range(len(my_lst))])    # 3-й способ
# print(my_lst, inv_lst_3)
if my_lst == inv_lst_3:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')



