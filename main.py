import numpy as np



def function(x):
    return x * np.sqrt(x ** 2 + 3)



def simpsons_method(lower_limit, upper_limit, number_of_intervals):
    if number_of_intervals % 2 == 1:
        raise ValueError("Number of intervals must be even.")

    step_size = (upper_limit - lower_limit) / number_of_intervals
    integral_value = function(lower_limit) + function(upper_limit)

    for index in range(1, number_of_intervals, 2):
        integral_value += 4 * function(lower_limit + index * step_size)

    for index in range(2, number_of_intervals - 1, 2):
        integral_value += 2 * function(lower_limit + index * step_size)

    integral_value *= step_size / 3
    return integral_value



lower_limit = 1
upper_limit = 2
number_of_intervals = 10


result = simpsons_method(lower_limit, upper_limit, number_of_intervals)
print(f"Approximate value of the integral: {result:.6f}")
