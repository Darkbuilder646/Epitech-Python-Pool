import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return x**2 + x*3 + 2

def plot_fct(func, min, max):
    xValue = np.linspace(min, max, 1000)
    yValue = [func(xi) for xi in xValue]

    plt.plot(xValue, yValue)

    plt.grid()
    plt.xlabel("Axis X")
    plt.ylabel("Axis Y")
    plt.title('Graphiques de f(x)')

    plt.show()
    

plot_fct(math.sin , 0, 50)
plot_fct(f, -100, 200)
plot_fct(lambda x: x**2 , -10, 10)
plot_fct(lambda x: 1/x, -100, 100)


