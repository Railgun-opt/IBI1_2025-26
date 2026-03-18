import matplotlib.pyplot as plt
Genes = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}
Genes["MYC"] = 11.6

plt.bar(Genes.keys(), Genes.values())
plt.xlabel("Genes")
plt.ylabel("Expression Levels")
plt.title("Gene Expression Levels")
plt.show()

Average_expression = sum(Genes.values()) / len(Genes)
print(f"Average gene expression level: {Average_expression:.2f}")