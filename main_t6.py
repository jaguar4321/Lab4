import numpy as np
import time


arr = np.array(list(map(int, input().split())))
a = time.time()

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i] = -1


print("Змінений масив:")
for i in range(len(arr)):
    print(arr[i], end=' ')

b = time.time()

print(f"creation time: {b - a} sec")



arr = np.array(list(map(int, input().split())))

a = time.time()


arr[arr != 0] = -1

print(arr)

b = time.time()
print(f"creation time numpy: {b - a} sec")
