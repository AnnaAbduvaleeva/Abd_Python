print('Введите четыре числа (суммы доходов за четыре квартала): ')
fst_quarter = float(input())
sec_quarter = float(input())
frd_quarter = float(input())
fth_quarter = float(input())
sum1 = fst_quarter + sec_quarter
sum2 = frd_quarter + fth_quarter
res = sum1 / sum2
print("%.3f" % res)