from matplotlib import pyplot as plt
import numpy as np
import math


def unary_():
    x = np.arange(0, 10, 0.1)
    y = x * 2
    plt.title("一元一次函数")
    plt.plot(x, y)
    plt.show()


def unary_quadratic_():
    x = np.arange(0, 10, 0.1)
    y = x ** 2 + 2 * x + 1
    plt.title("一元二次函数")
    plt.plot(x, y)
    plt.show()


def exponential_():
    x = np.arange(0, 10, 0.1)
    y = 2 ** x
    plt.title("指数函数")
    plt.plot(x, y)
    plt.show()


def natural_log_():
    x = np.arange(0, 10, 0.1)
    y = math.e ** x
    plt.title("指数函数")
    plt.plot(x, y)
    plt.show()


def sinusoidal_():
    x = np.linspace(-np.pi, np.pi, 100)
    y = np.sin(x)
    print(type(x))
    print(type(y))
    plt.title("正弦函数")
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    sinusoidal_()
