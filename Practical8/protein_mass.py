# protein_mass.py
# Given an amino acid sequence, calculate the total protein mass in amu.
# Returns an error message if any amino acid is not recognised.

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def protein_mass(sequence):
    """
    Calculate the total mass of a protein from its amino acid sequence.

    Args:
        sequence (str): string of single-letter amino acid codes

    Returns:
        float: total mass in atomic mass units (amu), or
        str: error message if an invalid amino acid is found
    """
    # residue masses from the Practical 8 guide table (monoisotopic, amu)
    aa_masses = {
        'G': 57.02,   # Glycine
        'A': 71.04,   # Alanine
        'S': 87.03,   # Serine
        'P': 97.05,   # Proline
        'V': 99.07,   # Valine
        'T': 101.05,  # Threonine
        'C': 103.01,  # Cysteine
        'I': 113.08,  # Isoleucine
        'L': 113.08,  # Leucine
        'N': 114.04,  # Asparagine
        'D': 115.03,  # Aspartic Acid
        'Q': 128.06,  # Glutamine
        'K': 128.09,  # Lysine
        'E': 129.04,  # Glutamic Acid
        'M': 131.04,  # Methionine
        'H': 137.06,  # Histidine
        'F': 147.07,  # Phenylalanine
        'R': 156.10,  # Arginine
        'Y': 163.06,  # Tyrosine
        'W': 186.08   # Tryptophan
    }

    sequence = sequence.upper().strip()
    total = 0.0

    for aa in sequence:
        if aa not in aa_masses:
            return f"Error: '{aa}' is not a valid amino acid."
        total += aa_masses[aa]

    return total


# ---- example calls ----
if __name__ == "__main__":
    print(protein_mass("ACDE"))       # normal case
    print(protein_mass("acde"))       # lowercase input
    print(protein_mass("ACX"))        # invalid amino acid
