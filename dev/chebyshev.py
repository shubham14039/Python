
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Poisson distribution parameter
mu = 25  # You can change this
epsilon = np.sqrt(mu) / 10
threshold = 0.01

# Range of n values (sample sizes)
n_values = np.arange(100, 20000, 500)
actual_probs = []
chebyshev_bounds = []

# Simulate and compute
num_trials = 10000

for n in n_values:
    samples = poisson.rvs(mu, size=(num_trials, n))
    sample_means = samples.mean(axis=1)
    errors = np.abs(sample_means - mu)
    actual_prob = np.mean(errors > epsilon)
    cheb_bound = 100 / n  # from earlier derivation

    actual_probs.append(actual_prob)
    chebyshev_bounds.append(cheb_bound)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, actual_probs, label='Simulated Probability of Large Error', linewidth=2)
plt.plot(n_values, chebyshev_bounds, label="Chebyshev's Upper Bound", linestyle='--', linewidth=2)
plt.axhline(y=threshold, color='red', linestyle=':', label='Target Threshold (0.01)')

plt.xlabel('Sample Size (n)')
plt.ylabel('Probability of Large Error')
plt.title(f'Chebyshev Bound vs Actual Error Probabilities (Poisson μ={mu})')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
