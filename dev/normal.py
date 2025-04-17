
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define parameters
mu = 0    # Mean
sigma = 1  # Standard deviation
x = np.linspace(-4, 4, 1000)

# Compute normal distribution PDF
y = norm.pdf(x, mu, sigma)

# Plot
plt.figure(figsize=(8,5))
plt.plot(x, y, label="Normal Distribution", color="blue")
plt.axvline(mu, color='black', linestyle='--', label="Mean (μ)")
plt.axvline(mu + sigma, color='red', linestyle='--', label="1σ")
plt.axvline(mu - sigma, color='red', linestyle='--')
plt.axvline(mu + 2*sigma, color='green', linestyle='--', label="2σ")
plt.axvline(mu - 2*sigma, color='green', linestyle='--')
plt.axvline(mu + 3*sigma, color='orange', linestyle='--', label="3σ")
plt.axvline(mu - 3*sigma, color='orange', linestyle='--')

plt.title("Normal Distribution with μ=0, σ=1")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()
