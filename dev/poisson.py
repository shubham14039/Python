import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def plot_poisson_distribution(lambda_val, k_range=None):
    """
    Plot the Poisson distribution for a given lambda value.
    
    Parameters:
    -----------
    lambda_val : float
        The rate parameter of the Poisson distribution (average number of events)
    k_range : tuple, optional
        Range of k values to plot as (min, max)
    """
    if k_range is None:
        # Set a reasonable k range based on lambda value
        k_min = 0
        k_max = max(10, int(lambda_val * 3))
    else:
        k_min, k_max = k_range
    
    # Generate k values
    k_values = np.arange(k_min, k_max + 1)
    
    # Calculate PMF for each k value
    pmf_values = poisson.pmf(k_values, lambda_val)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    
    # Bar plot for discrete distribution
    plt.bar(k_values, pmf_values, alpha=0.7, color='steelblue', label=f'λ = {lambda_val}')
    
    # Add stem lines to emphasize discrete nature
    markerline, stemlines, baseline = plt.stem(k_values, pmf_values, 
                                              linefmt='grey', markerfmt='o', 
                                              basefmt=' ')
    plt.setp(stemlines, 'linewidth', 0.8, 'alpha', 0.7)
    plt.setp(markerline, 'markersize', 4)
    
    # Add labels and title
    plt.xlabel('k (Number of Events)', fontsize=12)
    plt.ylabel('Probability P(X = k)', fontsize=12)
    plt.title(f'Poisson Distribution with λ = {lambda_val}', fontsize=14)
    plt.grid(alpha=0.3)
    plt.legend()
    
    # Show plot
    plt.tight_layout()
    plt.show()

# Example usage for different lambda values
if __name__ == "__main__":
    # Example 1: Low lambda value
    plot_poisson_distribution(1.5)
    
    # Example 2: Medium lambda value
    plot_poisson_distribution(5)
    
    # Example 3: High lambda value
    plot_poisson_distribution(15)
    
    # Example 4: Compare multiple lambda values on one plot
    lambdas = [2, 5, 10, 50]
    k_max = max(lambdas) * 3
    k_values = np.arange(0, k_max + 1)
    
    plt.figure(figsize=(12, 7))
    
    for lam in lambdas:
        pmf_values = poisson.pmf(k_values, lam)
        plt.plot(k_values, pmf_values, 'o-', label=f'λ = {lam}', alpha=0.7)
    
    plt.xlabel('k (Number of Events)', fontsize=12)
    plt.ylabel('Probability P(X = k)', fontsize=12)
    plt.title('Comparison of Poisson Distributions with Different λ Values', fontsize=14)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
