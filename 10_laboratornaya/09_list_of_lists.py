nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
external_lst = [nice_list[i][j][k] for i in range(2) for j in range(3) for k in range(3)]
print(external_lst)