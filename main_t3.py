import numpy as np
import time


n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))
r = int(input("Введіть кожен рядок"))
c = int(input("Введіть кожен стовпець"))



a = time.time()

arr = [[1 for j in range(m)] for i in range(n)]

for i in range(n):
    if i % r == 0:
        for j in range(m):
            arr[i][j] = 0
    for j in range(m):
        if j % c == 0:
            arr[i][j] = 0



# виводимо масив
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

b = time.time()


print(f"creation time: {b - a} sec")



n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))
r = int(input("Введіть кожен рядок"))
c = int(input("Введіть кожен стовпець"))

a = time.time()

matrix = np.ones((n, m), dtype=int)

matrix[::r, :] = 0
matrix[:, ::c] = 0


print(matrix)

b = time.time()

print(f"creation time numpy: {b - a} sec")
