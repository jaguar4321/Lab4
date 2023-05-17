import numpy as np
import time

A = [[5, 2, 0], [10, 4, 1], [7, 3, 2]]
B = [[3, 6, -1], [-1, -2, 0], [2, 1, 3]]

#(A - B**2) * (2A + B)

start_time = time.time()
C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[i])):
        value = (A[i][j] - B[i][j]**2) * (2*A[i][j] + B[i][j])
        row.append(value)
    C.append(row)
iterative_execution_time = time.time() - start_time

print("C -",C)



A = np.array([[5, 2, 0], [10, 4, 1], [7, 3, 2]])
B = np.array([[3, 6, -1], [-1, -2, 0], [2, 1, 3]])

start_time = time.time()
C_numpy = (A - B**2) * (2*A + B)
numpy_execution_time = time.time() - start_time
print(C_numpy)


are_equal = np.allclose(C_numpy, C)
print("відповіді однакові:",are_equal)

print("Час виконання з використанням NumPy:", numpy_execution_time)
print("Час виконання з використанням ітеративних конструкцій:", iterative_execution_time)