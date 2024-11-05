import numpy as np
import matplotlib.pyplot as plt

r1, r2, r3, r4 = 5, 4, 7, 2
l1, l2, l3 = 0.01, 0.02, 0.015
c1, c2, c3 = 300e-6, 150e-6, 200e-6

def modified_euler(u_max, f, t_integration, h):
    omega = 2 * np.pi * f
    t_values = np.arange(0, t_integration, h)
    u1 = u_max * np.sin(omega * t_values)

    i1, i2, i3 = 0, 0, 0
    u_c1, u_c2 = 0, 0

    u2_output = []

    for u_in in u1:
        di1_dt = (u_in - r1 * i1 - u_c1) / l1
        di2_dt = (u_c1 - r2 * i2 - u_c2) / l2
        di3_dt = (u_c2 - r3 * i3) / l3
        du_c1_dt = i1 / c1
        du_c2_dt = i2 / c2

        i1_star = i1 + h * di1_dt
        i2_star = i2 + h * di2_dt
        i3_star = i3 + h * di3_dt
        u_c1_star = u_c1 + h * du_c1_dt
        u_c2_star = u_c2 + h * du_c2_dt

        di1_star_dt = (u_in - r1 * i1_star - u_c1_star) / l1
        di2_star_dt = (u_c1_star - r2 * i2_star - u_c2_star) / l2
        di3_star_dt = (u_c2_star - r3 * i3_star) / l3
        du_c1_star_dt = i1_star / c1
        du_c2_star_dt = i2_star / c2

        i1 += 0.5 * h * (di1_dt + di1_star_dt)
        i2 += 0.5 * h * (di2_dt + di2_star_dt)
        i3 += 0.5 * h * (di3_dt + di3_star_dt)
        u_c1 += 0.5 * h * (du_c1_dt + du_c1_star_dt)
        u_c2 += 0.5 * h * (du_c2_dt + du_c2_star_dt)

        u2 = r4 * i3
        u2_output.append(u2)

    return t_values, np.array(u2_output)

t_values, u2_output = modified_euler(u_max=100, f=50, t_integration=0.2, h=0.00001)

plt.figure(figsize=(10, 6))
plt.plot(t_values, u2_output, label='$u_2$ (вихідна напруга)')
plt.title("перехідний процес вихідної напруги $u_2$ у rcl колі")
plt.xlabel("час (с)")
plt.ylabel("напруга $u_2$ (в)")
plt.grid(True)
plt.legend()
plt.show()
