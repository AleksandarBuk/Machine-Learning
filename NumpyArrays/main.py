import numpy as np

matrix = np.array([[1, 2, 3], #6
                   [4, 5, 6], # 15
                   [7, 8, 9]]) # 24

mean = np.mean(matrix)
# 45 / 9
# sum of features / number of features

matrix2 = np.array([[1, 2 , 3], # 6
                   [4, 5, 6]]) # 15

mean2 = np.mean(matrix2)
# 21 / 6 = 3.5

matrix3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]) # 126
matrix3_sum = np.sum(matrix3)
flattened_matrix = matrix3.flatten()
len_m3 = len(flattened_matrix)
print('Length of matrix3: ', len_m3)
print('M3 SUM:', matrix3_sum)
print('Manual mean calculation: ', matrix3_sum/len_m3)
mean3 = np.mean(matrix3)
# 126 / 18 = 7
print("Mean of the matrix:", mean)
print("Mean of the second matrix:", mean2)
print('Shape of the third matrix: ', matrix3.shape)
print("Mean of the third matrix:", mean3)
