import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані (константи)
R1, R2, R3, R4 = 5, 4, 7, 2           # Опори в Омах
L1, L2, L3 = 0.01, 0.02, 0.015         # Індуктивності в Генрі
C1, C2, C3 = 300e-6, 150e-6, 200e-6    # Ємності в Фарадах

def modified_euler(U_max, f, t_integration, h):

    # Кутова частота
    omega = 2 * np.pi * f

    # Масив часу
    t_values = np.arange(0, t_integration, h)
    U1 = U_max * np.sin(omega * t_values)  # Вхідна напруга як функція часу

    # Початкові значення
    I1, I2, I3 = 0, 0, 0  # Струми через індуктивності
    U_C1, U_C2 = 0, 0     # Напруги на конденсаторах

    # Місце для збереження результатів
    U2_output = []  # Напруга на виході U2

    # Основний цикл модифікованого методу Ейлера
    for U_in in U1:
        # Визначаємо похідні струмів та напруг
        dI1_dt = (U_in - R1 * I1 - U_C1) / L1
        dI2_dt = (U_C1 - R2 * I2 - U_C2) / L2
        dI3_dt = (U_C2 - R3 * I3) / L3
        dU_C1_dt = I1 / C1
        dU_C2_dt = I2 / C2

        # Прогнозний крок
        I1_star = I1 + h * dI1_dt
        I2_star = I2 + h * dI2_dt
        I3_star = I3 + h * dI3_dt
        U_C1_star = U_C1 + h * dU_C1_dt
        U_C2_star = U_C2 + h * dU_C2_dt

        # Коректорний крок
        dI1_star_dt = (U_in - R1 * I1_star - U_C1_star) / L1
        dI2_star_dt = (U_C1_star - R2 * I2_star - U_C2_star) / L2
        dI3_star_dt = (U_C2_star - R3 * I3_star) / L3
        dU_C1_star_dt = I1_star / C1
        dU_C2_star_dt = I2_star / C2

        # Оновлення значень методом модифікованого Ейлера
        I1 += 0.5 * h * (dI1_dt + dI1_star_dt)
        I2 += 0.5 * h * (dI2_dt + dI2_star_dt)
        I3 += 0.5 * h * (dI3_dt + dI3_star_dt)
        U_C1 += 0.5 * h * (dU_C1_dt + dU_C1_star_dt)
        U_C2 += 0.5 * h * (dU_C2_dt + dU_C2_star_dt)

        # Розрахунок вихідної напруги U2 на опорі R4
        U2 = R4 * I3
        U2_output.append(U2)

    return t_values, np.array(U2_output)

# Викликаємо функцію з заданими параметрами
t_values, U2_output = modified_euler(U_max=100, f=50, t_integration=0.2, h=0.00001)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(t_values, U2_output, label='$U_2$ (Output Voltage)', color='blue')
plt.title("Transient Response of Output Voltage $U_2$ in the RCL Circuit")
plt.xlabel("Time (s)")
plt.ylabel("Voltage $U_2$ (V)")
plt.grid(True)
plt.legend()
plt.show()
