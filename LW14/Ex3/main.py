import matplotlib.pyplot as plt
import numpy as np

# Визначаємо функцію
def Y(x):
    return 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

# Створюємо масив значень x від 0 до 5
x = np.linspace(0.0001, 5, 400)  # починаємо з 0.0001, щоб уникнути ділення на 0

# Обчислюємо значення Y(x) для кожного x
y = Y(x)

# Будуємо графік
plt.plot(x, y)
plt.title('Графік функції Y(x) = 5*cos(10*x)*sin(3*x)/sqrt(x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.grid(True)
plt.show()
