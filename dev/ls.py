import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    return 3*x -4

def fun2(x):
    return (x**2) + (2*x) - 15

def fun3(x):
    return 5*(x-1)*(x-2)*(x-3)

x_val = np.linspace(-20, 20, 400)
func = fun(x_val)
func2 = fun2(x_val)
func3 = fun3(x_val)
plt.plot(x_val, func, color="red")
plt.plot(x_val, func2, color="green")
# plt.plot(x_val, func3, color="blue")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Functions")
plt.show()
