import numpy as np
from matplotlib import pyplot as plt

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

def test_tabulation(f, a, b, n, axis):
    x, y = f(a, b, n)
    axis.plot(x, y)
    axis.grid()

def main():
    a, b, n = 0, N, 1000 

    fig, (ax1, ax2) = plt.subplots(2, 1)
    test_tabulation(tabulate_py, a, b, n, ax1)
    ax1.set_title('Tabulation with pure Python')
    test_tabulation(tabulate_np, a, b, n, ax2)
    ax2.set_title('Tabulation with Numpy')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
