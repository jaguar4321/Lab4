import numpy as np
import time


n = int(input("Введіть розмір матриці: "))

a = time.time()

matrix = [[1 for j in range(n)] for i in range(n)]



for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            matrix[i][j] = 0


for row in matrix:
    print(row)

b = time.time()

print(f"creation time: {b - a} sec")

n = int(input("Введіть розмір матриці: "))

a = time.time()

matrix = np.zeros((n, n), dtype=int)

matrix[:, 1::2] = 1


print(matrix)


b = time.time()

print(f"creation time numpy: {b - a} sec")