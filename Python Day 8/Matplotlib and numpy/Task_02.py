import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = [0, 1, 2, 3]
y = [12, 32, 42, 52]

plt.scatter(x,y,c= "red")
plt.grid()

plt.ylabel("some number")

plt.show()