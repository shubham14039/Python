import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create x and y coordinate arrays
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Compute z values - our function sin(x) + cos(y)
Z = np.sin(X) + np.cos(Y)

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.8,
                      linewidth=0, antialiased=True)

# Add color bar to show the mapping between colors and z values
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Set labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot of sin(x) + cos(y)')

# Add a contour plot projection on the bottom xy plane
offset = Z.min() - 0.5
ax.contour(X, Y, Z, zdir='z', offset=offset, cmap=cm.coolwarm)

# Adjust the view angle
ax.view_init(elev=30, azim=-45)

plt.tight_layout()
plt.show()
