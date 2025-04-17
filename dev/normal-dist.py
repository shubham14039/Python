import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def normal_distribution_demo(mu=0, sigma=1, sample_size=1000):
    """
    Generate and analyze a normal distribution with given parameters.
    
    Parameters:
    -----------
    mu : float
        Mean of the distribution
    sigma : float
        Standard deviation of the distribution
    sample_size : int
        Number of samples to generate
        
    Returns:
    --------
    dict
        Dictionary containing the samples and calculated statistics
    """
    # Generate samples from a normal distribution
    samples = np.random.normal(mu, sigma, sample_size)
    
    # Calculate statistics from the samples
    sample_mean = np.mean(samples)
    sample_variance = np.var(samples)
    sample_std = np.std(samples)
    
    # Calculate the theoretical probability density function (PDF)
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    pdf = stats.norm.pdf(x, mu, sigma)
    
    # Plot the histogram and PDF
    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Sample Histogram')
    plt.plot(x, pdf, 'r-', label=f'Normal PDF (μ={mu}, σ={sigma})')
    plt.axvline(sample_mean, color='b', linestyle='--', label=f'Sample Mean: {sample_mean:.4f}')
    plt.title('Normal Distribution Analysis')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    
    # Compare theoretical vs. sample statistics
    results = {
        'samples': samples,
        'theoretical': {
            'mean': mu,
            'variance': sigma**2,
            'std_dev': sigma
        },
        'empirical': {
            'mean': sample_mean,
            'variance': sample_variance,
            'std_dev': sample_std
        }
    }
    
    # Print statistics
    print(f"Theoretical Statistics:")
    print(f"  Mean (Expectation): {mu}")
    print(f"  Variance: {sigma**2}")
    print(f"  Standard Deviation: {sigma}")
    print(f"\nEmpirical Statistics (from samples):")
    print(f"  Mean: {sample_mean:.6f}")
    print(f"  Variance: {sample_variance:.6f}")
    print(f"  Standard Deviation: {sample_std:.6f}")
    
    return results

# Example usage
if __name__ == "__main__":
    # Test with different parameters
    results = normal_distribution_demo(mu=5, sigma=2, sample_size=10000)
    plt.show()
    
    # Manual calculation of normal distribution properties
    def manual_normal_pdf(x, mu, sigma):
        """Manual calculation of normal PDF without using scipy"""
        return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    # Generate values for a normal distribution
    mu, sigma = 0, 1
    x = np.linspace(-4, 4, 100)
    y = manual_normal_pdf(x, mu, sigma)
    
    # Plot manually calculated PDF
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'b-', label='Normal PDF')
    plt.title('Standard Normal Distribution (μ=0, σ=1)')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
