import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a 3D joint PMF for X, Y, Z ∈ {0, 1}
# Shape = (X, Y, Z)
joint_pmf = np.array([
    [[0.05, 0.05], [0.10, 0.10]],  # X = 0
    [[0.10, 0.10], [0.20, 0.30]]   # X = 1
])  # Total sum = 1.00 ✔

# Normalize (just in case)
joint_pmf /= joint_pmf.sum()

# Fix Z = 0 and Z = 1 to create 2D slices: P(X, Y | Z=z)
z_vals = [0, 1]
x_vals = [0, 1]
y_vals = [0, 1]

fig = plt.figure(figsize=(12, 5))

for i, z in enumerate(z_vals):
    ax = fig.add_subplot(1, 2, i+1, projection='3d')

    xpos, ypos = np.meshgrid(x_vals, y_vals, indexing="ij")
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)

    dx = dy = 0.4
    dz = joint_pmf[:, :, z].flatten()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)
    ax.set_title(f"P(X, Y | Z={z})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Probability")
    ax.set_xticks(x_vals)
    ax.set_yticks(y_vals)
    ax.set_zlim(0, max(dz)*1.2)

plt.tight_layout()
plt.show()
