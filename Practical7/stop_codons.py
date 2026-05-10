# stop_codons.py
# Read a yeast cDNA FASTA file, find genes that have at least one
# in-frame stop codon (TAA / TAG / TGA), and write them to a new
# FASTA file with the gene name and which stop codons were found.

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(SCRIPT_DIR, "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
outfile = os.path.join(SCRIPT_DIR, "stop_genes.fa")
STOP_CODONS = ('TAA', 'TAG', 'TGA')

# parse FASTA into a dict: gene_name -> sequence
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

# check each gene for in-frame stop codons (must start from ATG)
results = []
for gene_name, seq in genes.items():
    start_pos = seq.find('ATG')
    if start_pos == -1:
        continue

    found_stops = set()
    for i in range(start_pos, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in STOP_CODONS:
            found_stops.add(codon)

    if found_stops:
        stops_str = " ".join(sorted(found_stops))
        results.append((gene_name, seq, stops_str))

# write output FASTA
with open(outfile, 'w') as f:
    for gene_name, seq, stops_str in results:
        f.write(f">{gene_name} {stops_str}\n")
        for i in range(0, len(seq), 60):
            f.write(seq[i:i+60] + "\n")

print(f"Found {len(results)} gene(s) with in-frame stop codon(s).")
print(f"Results written to {outfile}")
