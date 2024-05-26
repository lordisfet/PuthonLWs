import matplotlib.pyplot as plt
import numpy as np

def Y(x):
    return 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

x = np.linspace(0.0001, 5, 400)

y = Y(x)

plt.plot(x, y)
plt.title('Графік функції Y(x) = 5*cos(10*x)*sin(3*x)/sqrt(x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.grid(True)
plt.show()