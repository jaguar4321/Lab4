import numpy as np

A = np.array([[1, 5, 3, -4],
              [3, 1, -2, 0],
              [5, -7, 0, 10],
              [0, 3, -5, 0]])

b = np.array([20, 9, -9, 1])


# Розмірність системи
n = A.shape[1]

# Обчислення определителя головної матриці A
det_A = np.linalg.det(A)


x = []

# Обчислення розв'язків системи за формулами Крамера
for i in range(n):
    # Створення копії головної матриці
    A_i = A.copy()
    # Заміна i-го стовпця на вектор b
    A_i[:, i] = b
    # Обчислення визначника матриці A_i
    det_Ai = np.linalg.det(A_i)
    # Розрахунок розв'язку xi
    xi = det_Ai / det_A
    x.append(xi)

# Виведення розв'язків системи
for i, xi in enumerate(x):
    print(f'x{i+1} = {xi}')


# Перевірка розв'язку за допомогою матричного множення
Ax = np.dot(A, x)
print('Перевірка за допомогою матричного множення:')
print(Ax)


# Обчислення розв'язку за допомогою оберненої матриці
A_inv = np.linalg.inv(A)
wrapped_matrix = np.dot(A_inv, b)
print('Перевірка за допомогою оберненої матриці:')
print(wrapped_matrix)



x_check = np.linalg.solve(A, b)
print('Перевірка за допомогою функції numpy.linalg.solve():')
print(x_check)

print("Рішення однакові:", np.allclose(b, Ax) and np.allclose(x, wrapped_matrix) and np.allclose(x, x_check))

