
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# Define x values (excluding non-positive integers where Gamma is undefined)
x = np.linspace(-4.9, 5, 500)
x = x[x != 0]  # remove zero to avoid division by zero in gamma

# Calculate Gamma(x)
y = gamma(x)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\Gamma(x)$', color='blue')
plt.ylim(-10, 10)  # focus on manageable y-range to avoid infinite poles
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Gamma Function")
plt.xlabel("x")
plt.ylabel(r"$\Gamma(x)$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
