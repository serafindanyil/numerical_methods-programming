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


matrix = [
    [8.3, 3.04, 4.1, 1.9],
    [3.92, 8.45, 7.36, 2.46],
    [3.77, 7.63, 8.04, 2.28],
    [2.21, 3.23, 1.69, 6.69],
]


print(f"Determinant is {gauss_determinant(matrix)}")
