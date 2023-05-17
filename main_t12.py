import numpy as np
import time

n = int(input("Введіть n: "))

a = time.time()


matrix = [[1 for j in range(n)] for i in range(n)]


for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            matrix[i][j] = 0


for row in matrix:
    print(row)

b = time.time()

print(f"creation time: {b - a} sec")


n = int(input("Введіть n: "))

a = time.time()
ones_array = np.ones((n, n))

ones_array[0, :] = 0
ones_array[n-1, :] = 0
ones_array[:, 0] = 0
ones_array[:, n-1] = 0

print(ones_array)
b = time.time()

print(f"creation time numpy: {b - a} sec")