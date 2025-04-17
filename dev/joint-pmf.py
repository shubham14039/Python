
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define possible values
x_vals = [0, 1]
y_vals = [0, 1]

# Joint PMF: p(x, y)
joint_pmf = np.array([
    [0.1, 0.2],  # p(X=0, Y=0), p(X=0, Y=1)
    [0.3, 0.4]   # p(X=1, Y=0), p(X=1, Y=1)
])

# Check normalization
print("Sum of all probabilities (should be 1):", joint_pmf.sum())

# Marginal PMFs
p_x = joint_pmf.sum(axis=1)  # Sum over y
p_y = joint_pmf.sum(axis=0)  # Sum over x

print("Marginal PMF of X:", dict(zip(x_vals, p_x)))
print("Marginal PMF of Y:", dict(zip(y_vals, p_y)))

# Visualize joint PMF
plt.figure(figsize=(6, 5))
sns.heatmap(joint_pmf, annot=True, xticklabels=y_vals, yticklabels=x_vals, cmap="Blues", fmt=".2f")
plt.title("Joint PMF of X and Y")
plt.xlabel("Y values")
plt.ylabel("X values")
plt.show()
