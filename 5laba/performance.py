import numpy as np
import matplotlib.pyplot as plt
import timeit

# Визначення N
N = 3

def func_py(x: list[float]) -> list[float]:
    return [1 - ((t - N/2) / (N/2)) ** 2 for t in x]

def tabulate_py(a: float, b: float, n: int) -> tuple:
    x = [a + i*(b - a)/n for i in range(n + 1)]
    y = func_py(x)
    return x, y

def tabulate_np(a: float, b: float, n: int) -> tuple:
    x = np.linspace(a, b, n + 1)
    y = 1 - ((x - N/2) / (N/2)) ** 2
    return x, y

def main():
    a, b, n = 0, N, 1000  # Оновл b до значення N

    n_values = np.array((1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000), dtype="uint32")
    t_py = np.full_like(n_values, 0, dtype='float')
    t_np = np.full_like(n_values, 0, dtype='float')

    for i in range(len(n_values)):
        t_py[i] = 1_000_000 * timeit.timeit(
            f"tabulate_py({a}, {b}, {n_values[i]})", 
            number=100, 
            globals=globals()
        ) / 100
        t_np[i] = 1_000_000 * timeit.timeit(
            f"tabulate_np({a}, {b}, {n_values[i]})", 
            number=100, 
            globals=globals()
        ) / 100

    plt.plot(n_values, t_py/t_np)
    plt.xlabel('Number of intervals')
    plt.ylabel('Python Time / Numpy Time')
    plt.title('Performance Comparison')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
