import numpy as np
import time


import random

n = int(input("Введіть розмір вектора: "))
a = time.time()


vector = [random.randint(0, 99) for i in range(n)]


unique_nums = set(vector)
count_unique_nums = len(unique_nums)


print("Випадковий вектор:", vector)
print("Кількість унікальних чисел у векторі:", count_unique_nums)

b = time.time()
print(f"creation time : {b - a} sec")



n = int(input("Введіть розмір вектора: "))

a = time.time()
arr = np.random.randint(0, 100, n)
unique_vals = np.unique(arr)

print("Випадковий вектор:", arr)
print("Кількість унікальних чисел у векторі:", len(unique_vals))

b = time.time()
print(f"creation time numpy: {b - a} sec")
