
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the scalar function
def f(x, y, z):
    return x**2 + y**2 + z**2

# Gradient (partial derivatives)
def df_dx(x, y, z):
    return 2 * x

def df_dy(x, y, z):
    return 2 * y

def df_dz(x, y, z):
    return 2 * z

# Create a 3D grid
grid_range = np.linspace(-2, 2, 5)
X, Y, Z = np.meshgrid(grid_range, grid_range, grid_range)

# Evaluate gradient at each point
U = df_dx(X, Y, Z)
V = df_dy(X, Y, Z)
W = df_dz(X, Y, Z)

# Plot the 3D gradient field
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Quiver: origin (X, Y, Z), vector (U, V, W)
ax.quiver(X, Y, Z, U, V, W, length=0.4, normalize=True, color='blue')

# Styling
ax.set_title("3D Gradient Field of f(x, y, z) = x² + y² + z²")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_box_aspect([1,1,1])
plt.tight_layout()
plt.show()
