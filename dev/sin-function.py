#NORMAL PLOT GRAPH
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Define grid range and resolution
x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
X, Y = np.meshgrid(x, y)

# 2. Compute function values
Z = np.sin(X**2 + Y**2)

# --- 3D Surface Plot ---
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title("3D Surface: sin(x² + y²)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")

# --- 2D Contour Plot ---
ax2 = fig.add_subplot(1, 2, 2)
contour = ax2.contourf(X, Y, Z, levels=100, cmap='viridis')
plt.colorbar(contour, ax=ax2)
ax2.set_title("Contour: sin(x² + y²)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

plt.tight_layout()
plt.show()

#INTERACTIVE PLOT USING PLOTLY
import numpy as np
import plotly.graph_objects as go

# Create a grid of x and y values
x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# Create the 3D surface plot
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
fig.update_layout(
    title="Interactive Plot: sin(x² + y²)",
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='f(x, y)'
    ),
    autosize=True,
    width=800,
    height=600
)

fig.show()
