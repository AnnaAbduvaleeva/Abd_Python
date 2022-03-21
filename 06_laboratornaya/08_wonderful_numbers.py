for i in range(10, 100):
    product_of_digits = (i % 10) * (i // 10)
    if i == 3 * product_of_digits:
        print(i)