# largest_orf.py
# Find the longest Open Reading Frame (ORF) in an RNA sequence.
# An ORF starts with AUG and ends at the nearest in-frame
# stop codon (UAA / UAG / UGA).

import re

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

STOP_CODONS = ('UAA', 'UAG', 'UGA')
longest = ""

# find every AUG in the sequence, then walk forward codon by codon
# until we hit a stop or run out of bases
for match in re.finditer(r'AUG', seq):
    start = match.start()
    for i in range(start, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in STOP_CODONS:
            orf = seq[start:i+3]
            if len(orf) > len(longest):
                longest = orf
            break

if longest:
    print(f"Longest ORF: {longest}")
    print(f"Length: {len(longest)} nucleotides")
else:
    print("No ORF found.")
