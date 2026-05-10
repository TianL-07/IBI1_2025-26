# Import library
import numpy as np
import matplotlib.pyplot as plt

# Create and print a dictionary with gene expression values
genes_dict = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}
print("Initial dictionary:", genes_dict)

# Add the gene 'MYC' with expression value 11.6
genes_dict['MYC'] = 11.6

# Expression value of a selected gene
#Pseudocode:
#1. select a gene of interest by changing the variable below
#2. check if the gene exists in the dictionary
#3. if gene exists: print its expression value
#4. if gene do not exist: print erroe message
gene_of_interest = "BRCA1"
print(f"\nGene of interest: {gene_of_interest}")
if gene_of_interest in genes_dict:
    print(f"Expression value for {gene_of_interest}: {genes_dict[gene_of_interest]}")
else:
    print(f"Error: Gene '{gene_of_interest}' not found in the dataset.")

# Average gene expression level
average_expression = sum(genes_dict.values()) / len(genes_dict)
print(f"Average gene expression level: {average_expression:.2f}")

# Produce a well-labelled bar chart
gene_names = list(genes_dict.keys())
expression_values = list(genes_dict.values())

plt.figure(figsize=(10, 6))
plt.bar(gene_names, expression_values, color='skyblue', edgecolor='navy')
plt.xlabel('Genes', fontsize=12)
plt.ylabel('Expression levels', fontsize=12)
plt.title('Gene Expression Levels', fontsize=14)
plt.grid(axis='y', alpha=0.3)

# Add value labels on top of bars
for i, v in enumerate(expression_values):
    plt.text(i, v + 0.2, str(v), ha='center', fontsize=10)

plt.tight_layout()
plt.show()
