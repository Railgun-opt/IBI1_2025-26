import matplotlib.pyplot as plt

# 1. create a dictionary with 5 genes and expression values
# 2. add MYC to the dictionary
# 3. print the dictionary
# 4. make a bar chart
# 5. pick a gene and print its value, if not found print error
# 6. calculate average expression

# create dictionary
Genes = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}

# add MYC
Genes["MYC"] = 11.6
print(Genes)

# bar chart
plt.bar(Genes.keys(), Genes.values())
plt.xlabel("Genes")
plt.ylabel("Expression Levels")
plt.title("Gene Expression Levels")
plt.show()

# check gene - change this to test different genes
gene_of_interest = "TP53"
if gene_of_interest in Genes:
    print(f"The expression level of {gene_of_interest} is {Genes[gene_of_interest]}.")
else:
    print(f"Error: '{gene_of_interest}' is not found in the dataset.")

# average
Average_expression = sum(Genes.values()) / len(Genes)
print(f"Average gene expression level: {Average_expression:.2f}")
