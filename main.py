import numpy as np
import matplotlib.pyplot as plt

# Параметри схеми для 21 варіанта
C1 = 1.5e-3  # Фарад
C2 = 2.9e-3  # Фарад
L_max = 15  # Генрі
L_min = 1.5  # Генрі
i_min = 1  # Ампер
i_max = 2  # Ампер
R1 = 13  # Ом
R2 = 73  # Ом
R3 = 22  # Ом
R4 = 31  # Ом
a = 0.001  # секунд
T = 6 * a  # Період сигналу

# Чисельні параметри
h = T / 400  # Крок інтегрування
steps_per_period = 100  # Точки на період

# Функція напруги живлення U1(t)
def U1(t):
    t_mod = t % T
    if t_mod <= T / 2:
        return 20 * t_mod / (T / 2) - 10
    else:
        return -20 * (t_mod - T / 2) / (T / 2) + 10

# Апроксимація індуктивності L2(i)
def L2(i2):
    if abs(i2) <= i_min:
        return L_max
    elif abs(i2) >= i_max:
        return L_min
    else:
        # Кубічний поліном для апроксимації
        a0, a1, a2, a3 = L_max, 0, (L_min - L_max) / ((i_max - i_min) ** 2), 0
        return a0 + a1 * abs(i2) + a2 * abs(i2)**2 + a3 * abs(i2)**3

# Система диференціальних рівнянь
def equations(t, y):
    uC1, uC2, i2 = y
    duC1_dt = (i2 - uC1 / R1) / C1
    duC2_dt = i2 / C2
    di2_dt = (U1(t) - uC1 - uC2 - i2 * (R2 + R4)) / L2(i2)
    return np.array([duC1_dt, duC2_dt, di2_dt])

# Метод Рунге-Кутта 3-го порядку
def runge_kutta_3_step(t, y):
    K1 = h * equations(t, y)
    K2 = h * equations(t + h / 2, y + K1 / 2)
    K3 = h * equations(t + h, y - K1 + 2 * K2)
    return y + (K1 + 4 * K2 + K3) / 6

# Симуляція системи
def simulate():
    t = 0
    y = np.array([0, 0, 0])  # Початкові умови: uC1, uC2, i2
    results = []

    for _ in range(5 * steps_per_period):
        uC1, uC2, i2 = y
        u2 = uC2 + i2 * R4
        u1 = U1(t)
        results.append([t, uC1, uC2, i2, u2, u1])
        y = runge_kutta_3_step(t, y)
        t += h

    return np.array(results)

# Виконання симуляції
results = simulate()

# Виділення результатів для графіків
t_values = results[:, 0]
uC1_values = results[:, 1]
uC2_values = results[:, 2]
i2_values = results[:, 3]
u2_values = results[:, 4]
u1_values = results[:, 5]

# Побудова графіків
plt.figure(figsize=(10, 6))
plt.plot(t_values, uC1_values, label="UC1(t)", color='b')
plt.title("UC1 / t")
plt.xlabel("Час (с)")
plt.ylabel("Напруга (В)")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_values, uC2_values, label="UC2(t)", color='m')
plt.title("UC2 / t")
plt.xlabel("Час (с)")
plt.ylabel("Напруга (В)")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_values, i2_values, label="I2(t)", color='c')
plt.title("I2 / t")
plt.xlabel("Час (с)")
plt.ylabel("Струм (А)")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_values, u2_values, label="U2(t)", color='g')
plt.title("U2 / t")
plt.xlabel("Час (с)")
plt.ylabel("Напруга (В)")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_values, u1_values, label="U1(t)", color='orange')
plt.title("U1 / t")
plt.xlabel("Час (с)")
plt.ylabel("Напруга (В)")
plt.grid(True)
plt.legend()
plt.show()

# Побудова графіка L2 / i
i_vals = np.linspace(-3, 3, 300)
l_vals = [L2(i) for i in i_vals]
plt.figure(figsize=(10, 6))
plt.plot(i_vals, l_vals, label="L2(I2)", color='r')
plt.title("L2 / I2")
plt.xlabel("Струм I2 (А)")
plt.ylabel("Індуктивність L2 (Гн)")
plt.grid(True)
plt.legend()
plt.show()
