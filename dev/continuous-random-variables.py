
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm
from scipy.integrate import quad
from rich.console import Console
from rich.table import Table

console = Console()

# Helper: Rich Table Printer
def display_table(headers, rows, title):
    table = Table(title=title)
    for header in headers:
        table.add_column(header, style="cyan")
    for row in rows:
        table.add_row(*[f"{x:.4f}" if isinstance(x, float) else str(x) for x in row])
    console.print(table)

# ------------------------------
# 🎯 Case 1: Y = sqrt(X), X ~ U(0,1)
# ------------------------------

x_vals = np.linspace(0, 1, 500)
f_X = lambda x: 1 if 0 <= x <= 1 else 0  # Uniform(0,1)
g = np.sqrt
g_inv = lambda y: y**2
g_inv_prime = lambda y: 2*y
f_Y = lambda y: 2*y if 0 <= y <= 1 else 0

y_vals = np.linspace(0, 1, 500)
fy_vals = np.array([f_Y(y) for y in y_vals])

plt.figure(figsize=(10, 4))
plt.plot(y_vals, fy_vals, label='f_Y(y) = 2y', color='green')
plt.title("PDF of Y = sqrt(X), X ~ U(0,1)")
plt.xlabel("y")
plt.ylabel("Density")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ------------------------------
# 🌀 Case 2: Y = X^2, X ~ N(0,1)
# ------------------------------

f_X2 = lambda x: norm.pdf(x)  # standard normal
f_Y2 = lambda y: (norm.pdf(np.sqrt(y)) + norm.pdf(-np.sqrt(y))) / (2 * np.sqrt(y)) if y > 0 else 0

y_vals2 = np.linspace(0.001, 5, 500)
fy2_vals = np.array([f_Y2(y) for y in y_vals2])

plt.figure(figsize=(10, 4))
plt.plot(y_vals2, fy2_vals, label='PDF of Y = X², X ~ N(0,1)', color='purple')
plt.title("PDF of Y = X² (Chi-squared with 1 d.o.f.)")
plt.xlabel("y")
plt.ylabel("Density")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ------------------------------
# 📊 Validation Table for Y = sqrt(X)
# ------------------------------
sample_points = np.linspace(0, 1, 6)
table_data = [(y, g_inv(y), f_X(g_inv(y)), g_inv_prime(y), f_Y(y)) for y in sample_points]

display_table(
    headers=["y", "x=g⁻¹(y)", "f_X(x)", "d/dy g⁻¹(y)", "f_Y(y)"],
    rows=table_data,
    title="Y = sqrt(X), Transformed PDF Table"
)
