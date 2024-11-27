import matplotlib.pyplot as plt
import numpy as np

C1 = 1.5e-3
C2 = 2.9e-3
L_max = 15
L_min = 1.5
i_min = 1
i_max = 2
R1 = 13
R2 = 73
R3 = 22
R4 = 31
a = 0.001
T = 6 * a
h = T / 400

x_points = []
y_points_u2 = []
y_points_u1 = []
x1_points = []
y1_points = []


def L2(i):
    if abs(i) <= i_min:
        return L_max
    elif abs(i) < i_max:
        normalized_i = (abs(i) - i_min) / (i_max - i_min)
        return L_max - (L_max - L_min) * (3 * normalized_i ** 2 - 2 * normalized_i ** 3)
    else:
        return L_min


def U1(t):
    phase = t % T
    if phase <= a:
        return 10 * phase / a
    elif phase <= 2 * a:
        return 10
    elif phase <= 3 * a:
        return 10 * (3 * a - phase) / a
    elif phase <= 4 * a:
        return -10 * (phase - 3 * a) / a
    elif phase <= 5 * a:
        return -10
    elif phase <= 6 * a:
        return -10 * (6 * a - phase) / a
    else:
        return 0


def system(t, x):
    uC1, uC2, iL2 = x
    duC1_dt = (iL2 - uC1 / R1) / C1
    duC2_dt = iL2 / C2
    diL2_dt = (U1(t) - uC1 - uC2 - iL2 * (R2 + R4)) / L2(iL2)
    return np.array([duC1_dt, duC2_dt, diL2_dt])


def runge_kutta_step(t, x):
    K1 = h * system(t, x)
    K2 = h * system(t + h / 3, x + K1 / 3)
    K3 = h * system(t + 2 * h / 3, x + 2 * K2 / 3)
    return x + (K1 + 3 * K3) / 4


def complex_lab():
    t = 0
    x = np.array([0, 0, 0])
    while t <= 5 * T:
        uC1, uC2, iL2 = x
        U2 = uC2 + iL2 * R4
        x_points.append(t)
        y_points_u2.append(U2)
        y_points_u1.append(U1(t))
        x = runge_kutta_step(t, x)
        t += h


def check_l():
    i_vals = np.linspace(0, 3, 300)
    for i in i_vals:
        x1_points.append(i)
        y1_points.append(L2(i))


complex_lab()
check_l()

plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points_u1, color='orange', label="U1(t)")
plt.title("Вхідна напруга U1(t)")
plt.xlabel("Час, с")
plt.ylabel("Напруга, В")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points_u2, color='g', label="U2(t)")
plt.title("Вихідна напруга U2(t)")
plt.xlabel("Час, с")
plt.ylabel("Напруга, В")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(x1_points, y1_points, color='r', label="L2(i)")
plt.title("Індуктивність L2(i)")
plt.xlabel("Струм, А")
plt.ylabel("Індуктивність, Гн")
plt.grid(True)
plt.legend()
plt.show()
