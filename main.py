import numpy as np
import time

N = ord('A') % 15 + 1
print(N)


# 1, 3, 4, 6,
# 10, 12, 15,
# 17, 18

n = int(input("Введіть розмір масиву: "))

a = time.time()
arr = [[0 for j in range(n)] for i in range(n)]


for i in range(n):
    arr[i][i] = i+1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()

b = time.time()

print(f"creation time: {b - a} sec")



n = int(input("Введіть розмірність масиву: "))

a = time.time()
arr = np.zeros((n, n), dtype=int)
arr = np.diag(np.arange(1, n+1))
print(arr)
b = time.time()

print(f"creation time numpy: {b - a} sec")
