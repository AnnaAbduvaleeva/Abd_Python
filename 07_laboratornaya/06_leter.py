import math

n = float(input('Введите размер письма: '))
print('Письмо нужно сложить', (math.ceil(math.log2(n / 12))) * 2, 'раза')