import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = [2, 4, 5, 9, 12, 20]
y = [1, 3, 5, 15, 20, 31]


def AddPointToChart(xValue: list, yValue: list):
    plt.scatter(xValue, yValue)

AddPointToChart(x,y)

plt.grid()
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.show()