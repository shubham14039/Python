
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the scalar function
def f(x, y):
    return np.sin(x) * np.cos(y)

# Define the partial derivatives (gradient components)
def df_dx(x, y):
    return np.cos(x) * np.cos(y)

def df_dy(x, y):
    return -np.sin(x) * np.sin(y)

# Create a grid
x = np.linspace(-2 * np.pi, 2 * np.pi, 20)
y = np.linspace(-2 * np.pi, 2 * np.pi, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Gradient (partial derivatives)
U = df_dx(X, Y)
V = df_dy(X, Y)
W = np.zeros_like(Z)  # No vertical component for gradient arrows (lie in xy-plane)

# Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, rstride=1, cstride=1, linewidth=0)

# Plot gradient vectors (quiver)
ax.quiver(X, Y, Z, U, V, W, color='red', length=0.5, normalize=True)

# Labels and style
ax.set_title('3D Gradient Field of f(x, y) = sin(x)·cos(y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

plt.tight_layout()
plt.show()
