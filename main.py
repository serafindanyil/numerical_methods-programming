import numpy as np


def function(x):
    return x * np.sqrt(x ** 2 + 3)  # Замінив оператор ^ на ** для піднесення до степеня


def simpson_method(borders, f, n):
    a, b = borders  # a - нижня межа, b - верхня межа

    func_a, func_b = f(a), f(b)

    h = (b - a) / n

    integral = 0

    # Метод для парних чисел
    if n % 2 != 0:
        n += 1

    # ітеруємось по н і перебираємо непарні точки
    for i in range(1, n // 2 + 1):
        x = a + (2 * i - 1) * h
        integral += 4 * f(x)

    # ітеруємось по н і перебираємо парні точки
    for i in range(1, n // 2):
        x = a + 2 * i * h
        integral += 2 * f(x)

    # Застосовуємо формулу сімпсона
    integral = (h / 3) * (func_a + func_b + integral)

    return integral


borders = [1, 2]

n = 100

# Обчислюємо результат
result = simpson_method(borders, function, n)

# Виводимо результат
print(f"Інтеграл: {result}")
