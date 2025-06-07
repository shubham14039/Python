
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Define the support of X and its PMF
x_vals = np.array([-2, -1, 0, 1, 2])
p_x = np.array([0.1, 0.2, 0.4, 0.2, 0.1])  # Must sum to 1

# Sample from X
np.random.seed(42)
samples_x = np.random.choice(x_vals, size=100000, p=p_x)

# Compute Y = X^2
samples_y = samples_x ** 2

# Compute empirical PMFs
pmf_x = Counter(samples_x)
pmf_y = Counter(samples_y)

# Normalize PMFs
for k in pmf_x:
    pmf_x[k] /= len(samples_x)
for k in pmf_y:
    pmf_y[k] /= len(samples_y)

# Plot PMFs
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# PMF of X
ax[0].bar(pmf_x.keys(), pmf_x.values(), color='skyblue')
ax[0].set_title("PMF of X")
ax[0].set_xlabel("x")
ax[0].set_ylabel("P(X = x)")

# PMF of Y = X^2
ax[1].bar(pmf_y.keys(), pmf_y.values(), color='salmon')
ax[1].set_title("PMF of Y = X^2")
ax[1].set_xlabel("y")
ax[1].set_ylabel("P(Y = y)")

plt.tight_layout()
plt.show()
