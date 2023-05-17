import numpy as np
import time


n = int(input("Введіть n: "))
m = int(input("Введіть m: "))

a = time.time()

matrix = []
for i in range(m):
    row = [0] * n
    if i == 0:
        row = list(range(n))
    matrix.append(row)

for row in matrix:
    print(row)

b = time.time()


print(f"creation time: {b - a} sec")



n = int(input("Введіть n: "))
m = int(input("Введіть m: "))

a = time.time()

matrix = np.zeros((m, n))
matrix[0] = np.arange(n)

print(matrix)

b = time.time()

print(f"creation time numpy: {b - a} sec")
