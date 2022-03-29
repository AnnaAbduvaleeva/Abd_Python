print('Введите четыре числа (суммы доходов за четыре квартала): ')
fst_quarter = float(input())
sec_quarter = float(input())
frd_quarter = float(input())
fth_quarter = float(input())
sum_1 = fst_quarter + sec_quarter
sum_2 = frd_quarter + fth_quarter
res = sum_1 / sum_2
print("%.3f" % res)
