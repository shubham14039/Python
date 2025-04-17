import numpy as np
import matplotlib.pyplot as plt

# Define x-axis (time values)
x = np.linspace(0, 10, 1000)

# Different lambda (rate) values to compare
lambdas = [0.5, 1.0, 2.0, 5.0]
colors = ['blue', 'green', 'orange', 'red']

plt.figure(figsize=(10, 6))

for lmbda, color in zip(lambdas, colors):
    # Exponential PDF
    y = lmbda * np.exp(-lmbda * x)
    plt.plot(x, y, label=f'λ = {lmbda}', color=color)

    # Plot vertical line for the mean = 1/λ
    mean = 1 / lmbda
    plt.axvline(mean, color=color, linestyle='--', alpha=0.7, label=f'Mean = {mean:.2f}')

# Beautify the plot
plt.title('Exponential Distribution - Varying λ', fontsize=16)
plt.xlabel('x (time)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
