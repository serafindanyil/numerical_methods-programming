# import numpy as np
#
#
# def determinant_gauss_with_partial_pivoting(matrix):
#     A = np.array(matrix, dtype=float)  # Копіюємо матрицю та перетворюємо в numpy масив
#     n = A.shape[0]  # Розмір матриці
#     det = 1.0  # Значення визначника
#
#     for k in range(n):
#         # Знаходження головного елемента
#         max_row = np.argmax(np.abs(A[k:n, k])) + k
#         if np.abs(A[max_row, k]) == 0:
#             return (
#                 0  # Якщо головний елемент дорівнює нулю, визначник також дорівнює нулю
#             )
#
#         # Обмін рядків
#         if max_row != k:
#             A[[k, max_row]] = A[[max_row, k]]
#             det *= -1  # Помноження на -1 для обліку зміни знаку
#
#         # Поступове перетворення матриці
#         for i in range(k + 1, n):
#             factor = A[i, k] / A[k, k]
#             A[i, k:] -= factor * A[k, k:]
#
#         # Оновлення значення визначника
#         det *= A[k, k]
#
#     return det
#
#
# # Приклад використання:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(f"Determinant: {determinant_gauss_with_partial_pivoting(matrix)}")

def gauss_determinant(matrix):
    n = len(matrix)
    det = 1.0

    # Прямий хід методу Гауса
    for k in range(n):
        if abs(matrix[k][k]) < 1e-12:
            # Якщо головний елемент близький до нуля, вважати, що матриця вироджена
            return 0.0

        # Множимо детермінант на головний елемент
        det *= matrix[k][k]

        # Приводимо рядки нижче головного елемента до нуля
        for i in range(k + 1, n):
            ratio = matrix[i][k] / matrix[k][k]
            for j in range(k, n):
                matrix[i][j] -= ratio * matrix[k][j]

    return det


# Тестування на прикладі заданої матриці
matrix = [[8.3, 3.04, 4.1, 1.9],
          [3.92, 8.45, 7.36, 2.46],
          [3.77, 7.63, 8.04, 2.28],
          [2.21, 3.23, 1.69, 6.69]]

det = gauss_determinant(matrix)

print(f"Determinant: {det}")


