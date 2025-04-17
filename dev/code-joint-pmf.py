
import numpy as np
import pandas as pd

# Possible values
x_vals = [0, 1]
y_vals = [0, 1]

# Joint PMF (p(X=x, Y=y))
joint_pmf = np.array([
    [0.1, 0.2],  # X = 0
    [0.3, 0.4]   # X = 1
])

# Create DataFrame for easier handling
df_joint = pd.DataFrame(joint_pmf, index=x_vals, columns=y_vals)
df_joint.index.name = "X"
df_joint.columns.name = "Y"

print("👉 Joint PMF (P(X, Y)):")
print(df_joint)

# Marginal PMFs
p_x = df_joint.sum(axis=1)  # Sum over Y
p_y = df_joint.sum(axis=0)  # Sum over X

print("\n👉 Marginal PMF of X (P(X)):")
print(p_x)

print("\n👉 Marginal PMF of Y (P(Y)):")
print(p_y)

# Conditional PMF: P(X | Y)
cond_p_x_given_y = df_joint.div(p_y, axis=1)

print("\n👉 Conditional PMF P(X | Y):")
print(cond_p_x_given_y)

# Conditional PMF: P(Y | X)
cond_p_y_given_x = df_joint.div(p_x, axis=0)

print("\n👉 Conditional PMF P(Y | X):")
print(cond_p_y_given_x)
