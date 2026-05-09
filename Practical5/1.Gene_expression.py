# Create and print a dictionary containing the genes and their expression values
genes = {
    'TP53':12.4, 
    'EGFR':15.1, 
    'BRCA1':8.2, 
    'PTEN':5.3, 
    'ESR1':10.7
}
print(genes)
# Add the gene 'MYC' to the dictionary with an expression value of 11.6
genes['MYC']=11.6
'MYC' in genes
# Produce a well-labelled bar chart showing the expression values of all genes
import numpy as np
import matplotlib.pyplot as plt
genes = list(genes.keys())
expressions = list(genes.values())
plt.figure(figsize=(10, 6))
plt.bar(genes, expressions, color='skyblue', edgecolor='navy')
plt.xlable('genes', fontsize=12)
plt.ylabel('expressions', fontsize=12)
plt.title('gene_expression', fontsize=14)
plt.grid(axis='y', alpha=0.3)
# Add value labels on top of bars
for i, v in enumerate('gene_expression'):
    plt.text(i, v + 0.2, str(v), ha='center', fontsize=10)

plt.tight_layout()
plt.show()

# Create a variable representing a gene of interest
# PSEUDOCODE: Change the value of 'gene_of_interest' to test different genes
gene_of_interest = "BRCA1"
print(f"Gene of interest: {gene_of_interest}")
if gene_of_interest in genes:
    print(f"Expression value for {gene_of_interest}: {genes[gene_of_interest]}")
else:
    print(f"Error: Gene '{gene_of_interest}' not found in the dataset.")
print()

# Calculate the average gene expression level across all genes
average_expression = sum(genes.values()) / len(genes)
print(f"Average gene expression level: {average_expression:.2f}")

