import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. Ensure the results directory exists (Code Ocean usually provides it, 
# but this is good practice)
os.makedirs('../results', exist_ok=True)

# 2. Load the data
df = pd.read_csv('../data/sample_expression.csv')

# 3. Simple Transformation (Log2 fold change approximation)
# We add 1 to avoid log(0) errors
df['mean_samples'] = df[['sample_A', 'sample_B']].mean(axis=1)
df['log2_ratio'] = (df['mean_samples'] + 1) / (df['control'] + 1)

# 4. Generate a Visualization
plt.figure(figsize=(8, 5))
plot = sns.barplot(data=df, x='gene_id', y='log2_ratio', hue='gene_type')
plt.xticks(rotation=45, ha='right')
plt.title("Relative Gene Expression (Sample vs Control)")
plt.tight_layout()

# 5. SAVE TO RESULTS (The most important part of the demo!)
plt.savefig('../results/expression_analysis.png')

print("Analysis complete. Check the /results folder for the plot!")
