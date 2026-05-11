# count_codons.py
# Ask the user for a stop codon (TAA / TAG / TGA), then find all genes
# containing that stop codon in-frame, extract the coding region up to
# the longest ORF for each gene, count every codon across all those
# regions, write the counts to a file, and plot a bar chart.

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# the FASTA data file lives on the external drive, not in the repo
DATA_DIR = "/Volumes/MOVESPEED/IBI/Week 7 Python III Working with Strings and Files"
filename = os.path.join(DATA_DIR, "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
count_file = os.path.join(SCRIPT_DIR, "codon_counts.txt")
pie_file = os.path.join(SCRIPT_DIR, "codon_pie_chart.png")
VALID_STOPS = ('TAA', 'TAG', 'TGA')

# ask user which stop codon to search for
user_stop = input("Enter a stop codon (TAA/TAG/TGA): ").upper().strip()
if user_stop not in VALID_STOPS:
    print("Invalid stop codon. Please enter TAA, TAG, or TGA.")
    exit()

# parse FASTA into {gene_name: sequence}
genes = {}
current_gene = ""
current_seq = ""

with open(filename, 'r') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('>'):
            if current_gene:
                genes[current_gene] = current_seq
            current_gene = line[1:].split()[0]
            current_seq = ""
        else:
            current_seq += line
    if current_gene:
        genes[current_gene] = current_seq

# for each gene that has user_stop, take the longest ORF
# (scan ALL occurrences, don't stop at the first one)
coding_seqs = {}
for gene_name, seq in genes.items():
    start_pos = seq.find('ATG')
    if start_pos == -1:
        continue

    best_orf = ""
    for i in range(start_pos, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon == user_stop:
            orf = seq[start_pos:i+3]
            if len(orf) > len(best_orf):
                best_orf = orf

    if best_orf:
        coding_seqs[gene_name] = best_orf

# count every codon across all coding sequences
codon_counts = {}
for gene_name, coding_seq in coding_seqs.items():
    for i in range(0, len(coding_seq) - 2, 3):
        codon = coding_seq[i:i+3]
        if len(codon) == 3:
            codon_counts[codon] = codon_counts.get(codon, 0) + 1

# write counts to file (sorted alphabetically by codon)
with open(count_file, 'w') as f:
    f.write("Codon\tCount\n")
    for codon in sorted(codon_counts.keys()):
        f.write(f"{codon}\t{codon_counts[codon]}\n")

print(f"Found {len(coding_seqs)} genes with {user_stop} stop codon.")
print(f"Counted {len(codon_counts)} unique codons.")
print(f"Counts saved to {count_file}")

# draw a pie chart of codon usage
# with 64 codons, putting labels directly on each slice causes overlap,
# so we leave the slices unlabelled and put a legend outside the chart instead
labels = list(codon_counts.keys())
sizes = list(codon_counts.values())

fig, ax = plt.subplots(figsize=(14, 10))
wedges, texts, autotexts = ax.pie(
    sizes,
    autopct=lambda p: f'{p:.1f}%' if p > 1.5 else '',  # only label slices > 1.5%
    textprops={'fontsize': 7},
    startangle=90
)
ax.legend(
    wedges, labels,
    title="Codon",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=7
)
ax.set_title(
    f"Codon Usage for genes ending with {user_stop}\n"
    f"(in-frame codons, n={sum(sizes):,})",
    fontsize=13
)
plt.savefig(pie_file, dpi=150, bbox_inches='tight')
plt.close()

print(f"Pie chart saved to {pie_file}")
