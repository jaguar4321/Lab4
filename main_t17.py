import numpy as np
import time


n = int(input("Введіть розмір вектора: "))

a = time.time()

vector = [i for i in range(n + 1)]
print(vector)

for i in range(n + 1):
    if vector[i] < n/2 or vector[i] > 3*n/4:
        vector[i] *= -1


print(vector)

b = time.time()

print(f"creation time: {b - a} sec")


n = int(input("Введіть розмір вектора: "))

a = time.time()

vec = np.arange(n + 1)

vec[(vec < n/2) | (vec > 3*n/4)] *= -1

print(vec)

b = time.time()
print(f"creation time numpy: {b - a} sec")


