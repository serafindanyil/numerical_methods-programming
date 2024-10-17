def first_function(x1, x2):
    return x1 ** 2 + x2 ** 2 + 0.1 + x1


def second_function(x1, x2):
    return 2 * x1 * x2 + 0.1 + x2


# Метод Гауса
def gauss_elimination(A, b):
    n = len(b)

    # Прямий хід (обертання з вибором головного елемента по стовпцю)
    for i in range(n):
        # Знаходимо головний елемент
        max_row = i + max(range(n - i), key=lambda k: abs(A[i + k][i]))

        # Обмінюємо рядки
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Прямий хід Гауса
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Зворотній хід для знаходження розв'язку
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]

    return x


# Метод січних (без обчислення явного Якобіана)
def secant_method(x1, x2, tol=1e-5, max_iter=100):
    h = 1e-5  # Малий крок для числового обчислення похідної
    for _ in range(max_iter):
        # Обчислюємо значення функцій
        f_val = [first_function(x1, x2), second_function(x1, x2)]

        # Перевірка умови збіжності
        if abs(f_val[0]) < tol and abs(f_val[1]) < tol:
            return x1, x2

        # Числове обчислення похідних (секущі)
        df1_dx1 = (first_function(x1 + h, x2) - first_function(x1, x2)) / h
        df1_dx2 = (first_function(x1, x2 + h) - first_function(x1, x2)) / h
        df2_dx1 = (second_function(x1 + h, x2) - second_function(x1, x2)) / h
        df2_dx2 = (second_function(x1, x2 + h) - second_function(x1, x2)) / h

        # Створюємо матрицю якобіана (якобіан числовий)
        J = [[df1_dx1, df1_dx2], [df2_dx1, df2_dx2]]

        # Застосовуємо метод Гауса для розв'язання лінійної системи
        delta_x = gauss_elimination(J, [-f_val[0], -f_val[1]])

        # Оновлюємо значення x1 і x2
        x1 += delta_x[0]
        x2 += delta_x[1]

    raise ValueError("Не збігається за задану кількість ітерацій")


# Початкові наближення
x1_initial = 0.0
x2_initial = 0.0

# Запуск методу січних
solution = secant_method(x1_initial, x2_initial)
print(f"Розв'язок: x1 = {solution[0]}, x2 = {solution[1]}", )
print("Перевірка: ")
print(first_function(solution[0], solution[1]))
print(second_function(solution[0], solution[1]))
