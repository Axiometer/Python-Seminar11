import numpy as np
import matplotlib.pyplot as plt

# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

a, b, c, d, e = -12, -18, 5, 10, -30
x = np.arange(48, 53, 0.001)
x_cut = np.arange(48, 53, 0.001)

def func(x):
    function = a*np.sin(np.cos(x))*x**4 + b*x**3 + c*x**2 + d*x + e
    return function

root1 = 48
root2 = 53
for i in np.arange(48, 50, 0.001):
    if np.absolute(func(root1))>np.absolute(func(i)):
        root1 = i
print(root1)
for i in np.arange(50, 53, 0.001):
    if np.absolute(func(root2))>np.absolute(func(i)):
        root2 = i
print(root2)

min_func = min(func(x_cut))

def extr_func(x, min_func):
    extremum_function = a*np.sin(np.cos(x))*x**4 + b*x**3 + c*x**2 + d*x + e - min_func
    return  extremum_function

extr_x_cut = 48
for i in np.arange(48, 53, 0.001):
    if np.absolute(extr_func(extr_x_cut, min_func))>np.absolute(extr_func(i, min_func)):
        extr_x_cut = i

x_range_down = np.arange(48, extr_x_cut, 0.001)
x_range_up = np.arange(extr_x_cut, 53, 0.001)
plt.title(f'Корни функции на участке (48; 53): {round(root1, 3)}, {round(root2, 3)}')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
plt.plot(x, func(x), 'g')
plt.plot(x_range_down, func(x_range_down), 'r', label="Убывание")
plt.plot(x_range_up, func(x_range_up), 'b', label="Возрастание")
plt.text(extr_x_cut, func(extr_x_cut) + 30, f'Вершина функции x = {round(extr_x_cut, 2)}')
plt.scatter([root1, root2], [root2, root1], c='#000000')
plt.legend()
plt.show()