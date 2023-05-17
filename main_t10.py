import numpy as np
import time
import random
import math

n = int(input("Введіть n: "))
m = int(input("Введіть m: "))

a = time.time()


matrix = [[random.randint(0, 100) for j in range(m)] for i in range(n)]


min_val = matrix[0][0]
max_val = matrix[0][0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]


sum_val = 0
for i in range(n):
    for j in range(m):
        sum_val += matrix[i][j]

avg_val = sum_val / (n * m)


squared_diff_sum = 0
for i in range(n):
    for j in range(m):
        squared_diff_sum += (matrix[i][j] - avg_val) ** 2

std_dev = math.sqrt(squared_diff_sum / (n * m))


print("Мінімальне значення:", min_val)
print("Максимальне значення:", max_val)
print("Середнє значення:", round(avg_val, 3))
print("Середньо квадратичне відхилення:", round(std_dev, 3))

b = time.time()

print(f"creation time: {b - a} sec")


n = int(input("Введіть n: "))
m = int(input("Введіть m: "))


arr = np.random.rand(n, m)


arr_min = arr.min()
arr_max = arr.max()


arr_mean = arr.mean()
arr_std = arr.std()


print("Мінімальне значення: {:.3f}".format(arr_min))
print("Максимальне значення: {:.3f}".format(arr_max))
print("Середнє значення: {:.3f}".format(arr_mean))
print("Середньо квадратичне відхилення: {:.3f}".format(arr_std))

b = time.time()

print(f"creation time numpy: {b - a} sec")
