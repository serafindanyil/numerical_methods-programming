# Метод поділу
# ділянки навпіл
def bisection_method(function, interval):
    a, b = interval
    epsilon = 0.001
    if function(a) * function(b) >= 0:
        print("Функція повинна змінювати знак на кінцях інтервалу [a, b].")
        return None

    while (b - a) / 2 > epsilon:
        x = (a + b) / 2
        if function(x) == 0:
            return x
        elif function(a) * function(x) < 0:
            b = x
        else:
            a = x

    return x

# Визначення функції
func = lambda x: x**3 + 6*x**2 + 9*x + 1

# Границі інтервалу
array = [-1, 1]

# Знаходження кореня
root = bisection_method(func, array)
print("Приближене значення кореня:", func(root))