import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=50, scale=10, size=1000)  # Mean=50, StdDev=10, Sample size=1000
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title("Histogram of Randomly Generated Normal Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
