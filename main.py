import numpy as np


def f1(x1, x2):
    return x1 ** 2 + x2 ** 2 + 0.1 + x1


def f2(x1, x2):
    return 2 * x1 * x2 + 0.1 + x2



def jacobian(x1, x2, h=1e-6):
    df1_dx1 = (f1(x1 + h, x2) - f1(x1, x2)) / h
    df1_dx2 = (f1(x1, x2 + h) - f1(x1, x2)) / h
    df2_dx1 = (f2(x1 + h, x2) - f2(x1, x2)) / h
    df2_dx2 = (f2(x1, x2 + h) - f2(x1, x2)) / h
    return np.array([[df1_dx1, df1_dx2], [df2_dx1, df2_dx2]])


# Secant method to solve the system
def secant_method(x1_0, x2_0, tol=1e-6, max_iter=100):
    x1, x2 = x1_0, x2_0
    for i in range(max_iter):
        F = np.array([f1(x1, x2), f2(x1, x2)])
        J = jacobian(x1, x2)

        # Gaussian elimination to solve J * delta_x = -F
        try:
            delta_x = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("Jacobian is singular, cannot proceed.")
            return None

        x1 += delta_x[0]
        x2 += delta_x[1]

        # Check for convergence
        if np.linalg.norm(delta_x) < tol:
            print(f"Converged after {i + 1} iterations")
            return x1, x2

    print("Maximum iterations exceeded")
    return None



x1_0, x2_0 = 0.0, 0.0
solution = secant_method(x1_0, x2_0)

print(f"Solution: x1 = {solution[0]}, x2 = {solution[1]}")
