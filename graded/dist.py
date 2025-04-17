
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import geom

# Set style for better visualization
sns.set(style="whitegrid")

# Define possible values of X
x = np.arange(1, 15)  # X can take values from 1 to 14 for visualization

# Define different success probabilities
p_values = [0.2, 0.4, 0.6]  # Different probabilities of success

# Plot Geometric PMF for different p values
plt.figure(figsize=(8, 5))

for p in p_values:
    y = geom.pmf(x, p)  # Compute the probability mass function
    plt.plot(x, y, 'o-', label=f'p = {p}')

plt.xlabel("Number of Trials (X)")
plt.ylabel("P(X = k)")
plt.title("Geometric Distribution PMF for Different p Values")
plt.legend()
plt.show()
