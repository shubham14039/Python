
import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()

def display_table(df, title):
    table = Table(title=title)
    for col in df.columns:
        table.add_column(str(col), style="cyan", justify="center")
    for _, row in df.iterrows():
        table.add_row(*[str(round(val, 4)) if isinstance(val, float) else str(val) for val in row])
    console.print(table)

movie_data = {
    'Age Group': ['<18', '18-35', '35+'],
    'Like (Y=1)': [0.10, 0.30, 0.15],
    'Dislike (Y=0)': [0.05, 0.10, 0.30]
}
df_movie = pd.DataFrame(movie_data)

# Flatten to long format
movie_long = df_movie.melt(id_vars='Age Group', var_name='Like', value_name='Joint_PMF')
movie_long['Y'] = movie_long['Like'].map({'Like (Y=1)': 1, 'Dislike (Y=0)': 0})

# Marginal P(Y)
p_y = movie_long.groupby('Y')['Joint_PMF'].sum().to_dict()

# Conditional PMF: P(Age | Like)
cond_movie = movie_long[movie_long['Y'] == 1].copy()
cond_movie['P(Age | Like=1)'] = cond_movie['Joint_PMF'] / p_y[1]

display_table(cond_movie[['Age Group', 'Joint_PMF', 'P(Age | Like=1)']], "🎬 Conditional PMF: P(Age | Liked Movie)")


spam_data = {
    'Word "free" Present': ['Yes', 'No'],
    'Spam (Y=1)': [0.30, 0.20],
    'Not Spam (Y=0)': [0.05, 0.45]
}
df_spam = pd.DataFrame(spam_data)

# Flatten
spam_long = df_spam.melt(id_vars='Word "free" Present', var_name='Spam', value_name='Joint_PMF')
spam_long['Y'] = spam_long['Spam'].map({'Spam (Y=1)': 1, 'Not Spam (Y=0)': 0})

# Marginal P("free")
p_free = spam_long.groupby('Word "free" Present')['Joint_PMF'].sum().to_dict()

# Conditional PMF: P(Spam | "free" = Yes)
cond_spam = spam_long[spam_long['Word "free" Present'] == 'Yes'].copy()
cond_spam['P(Spam | "free")'] = cond_spam['Joint_PMF'] / p_free['Yes']

display_table(cond_spam[['Word "free" Present', 'Spam', 'Joint_PMF', 'P(Spam | "free")']], '📧 Conditional PMF: P(Spam | "free") Present')
