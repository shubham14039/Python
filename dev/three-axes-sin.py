import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D axis
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Create 3D grid of points
x = np.linspace(-2*np.pi, 2*np.pi, 15)
y = np.linspace(-2*np.pi, 2*np.pi, 15)
z = np.linspace(-2*np.pi, 2*np.pi, 15)
X, Y, Z = np.meshgrid(x, y, z)

# Calculate the value of sin(x) + sin(y) + sin(z)
values = np.sin(X) + np.sin(Y) + np.sin(Z)

# We'll visualize 4D data using a 3D scatter plot
# where color and size represent the 4th dimension (function value)
points = np.column_stack([X.flatten(), Y.flatten(), Z.flatten()])
values_flat = values.flatten()

# Normalize values to range 0-1 for color mapping
norm = plt.Normalize(values_flat.min(), values_flat.max())

# Create scatter plot with colors representing function values
scatter = ax.scatter(
    points[:, 0], points[:, 1], points[:, 2],
    c=values_flat, cmap=cm.viridis,
    s=100 * (norm(values_flat) + 0.1),  # Size based on value (with minimum size)
    alpha=0.7
)

# Add a color bar
cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('sin(x) + sin(y) + sin(z) value')

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('4D Visualization of sin(x) + sin(y) + sin(z)')

# Set axis limits
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-2*np.pi, 2*np.pi)
ax.set_zlim(-2*np.pi, 2*np.pi)

# Add a grid for better spatial reference
ax.grid(True)

plt.tight_layout()
plt.show()

# Alternative visualization: 3D slices at different z-values
fig2 = plt.figure(figsize=(15, 10))

# We'll create 4 slices of the 4D function at different z values
z_values = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]

for i, z_val in enumerate(z_values, 1):
    # Create a subplot
    ax = fig2.add_subplot(2, 3, i, projection='3d')
    
    # Create a 2D grid for x and y
    x = np.linspace(-2*np.pi, 2*np.pi, 50)
    y = np.linspace(-2*np.pi, 2*np.pi, 50)
    X, Y = np.meshgrid(x, y)
    
    # Calculate sin(x) + sin(y) + sin(z) with z fixed at z_val
    Z = np.sin(X) + np.sin(Y) + np.sin(z_val)
    
    # Create the surface plot
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.8,
                       linewidth=0, antialiased=True)
    
    # Add a colorbar
    fig2.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Function value')
    ax.set_title(f'Slice at z = {z_val:.2f}')
    
    # Set consistent z-axis limits for comparison
    ax.set_zlim(-3, 3)

plt.suptitle('3D Slices of sin(x) + sin(y) + sin(z) at Different z Values', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
