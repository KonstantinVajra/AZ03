import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(50)  # 50 случайных чисел для оси X
y = np.random.rand(50)  # 50 случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
