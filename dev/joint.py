import pandas as pd
from rich.console import Console
from rich.table import Table

# Create console
console = Console()

# Input data
data = {
    'X': [0, 0, 1, 1, 2, 2],
    'Y': [0, 1, 0, 1, 0, 1],
    'Count': [20, 5, 25, 15, 10, 25]
}

df = pd.DataFrame(data)
total = df['Count'].sum()
df['Joint_PMF'] = df['Count'] / total

# Marginals
marginal_X = df.groupby('X')['Joint_PMF'].sum().reset_index(name='P_X')
marginal_Y = df.groupby('Y')['Joint_PMF'].sum().reset_index(name='P_Y')
df = df.merge(marginal_X, on='X').merge(marginal_Y, on='Y')

# Conditional PMFs
df['P_X_given_Y'] = df['Joint_PMF'] / df['P_Y']
df['P_Y_given_X'] = df['Joint_PMF'] / df['P_X']
df['P_X*P_Y'] = df['P_X'] * df['P_Y']
df['Independent'] = (df['Joint_PMF'].round(4) == df['P_X*P_Y'].round(4))

# Rich table
table = Table(title="🔍 Joint & Marginal PMF Analysis")

# Define columns
columns = ['X', 'Y', 'Joint_PMF', 'P_X', 'P_Y', 'P_X_given_Y', 'P_Y_given_X', 'P_X*P_Y', 'Independent']
for col in columns:
    table.add_column(col, justify="center", style="bold green" if col == 'Independent' else "cyan")

# Add rows
for _, row in df.iterrows():
    table.add_row(
        str(row['X']),
        str(row['Y']),
        f"{row['Joint_PMF']:.4f}",
        f"{row['P_X']:.4f}",
        f"{row['P_Y']:.4f}",
        f"{row['P_X_given_Y']:.4f}",
        f"{row['P_Y_given_X']:.4f}",
        f"{row['P_X*P_Y']:.4f}",
        "[green]True[/green]" if row['Independent'] else "[red]False[/red]"
    )

# Render table
console.print(table)
