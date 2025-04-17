from scipy.stats import hypergeom, geom
import numpy as np
import matplotlib.pyplot as plt
# Define hypergeometric parameters
N = 100  # Total dataset size
K = 40   # Number of "good" (relevant) features in the dataset
n = 10   # Sample size (features we pick)
x = np.arange(0, n+1)

# Compute probability mass function (PMF)
pmf = hypergeom.pmf(x, N, K, n)

# Plot the PMF
plt.bar(x, pmf, color='green', alpha=0.7, edgecolor='black')
plt.xlabel("Number of Relevant Features Selected")
plt.ylabel("Probability")
plt.title("Hypergeometric Distribution (Feature Selection)")
plt.grid()
plt.show()

# Geometric distribution
# Define probability of success (e.g., probability of an RL agent learning an optimal action)
p = 0.3

# Generate geometric random samples
samples = geom.rvs(p, size=10000)

# Plot the distribution
plt.hist(samples, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel("Number of Trials Until First Success")
plt.ylabel("Probability")
plt.title("Geometric Distribution (p = 0.3)")
plt.grid()
plt.show()
