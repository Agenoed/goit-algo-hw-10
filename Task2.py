import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# --- Метод Монте-Карло ---

def monte_carlo_integration(func, a, b, n):
    sum_y = 0
    for _ in range(n):
        x = random.uniform(a, b)
        sum_y += func(x)
    return (b - a) * sum_y / n

# Кількість випадкових точок
n = 100000

result_mc = monte_carlo_integration(f, a, b, n)
print(f"Результат (Монте-Карло): {result_mc}")

# --- Перевірка за допомогою SciPy ---

result_quad, error_quad = spi.quad(f, a, b)
print(f"Результат (SciPy): {result_quad}, Похибка: {error_quad}")

# --- Візуалізація ---

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()