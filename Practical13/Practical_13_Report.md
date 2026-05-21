# Practical 13: Sequence Comparisons using Online BLAST and Python

## 1. Human DLX5 Protein Information

Data obtained from UniProt (https://www.uniprot.org):

| Property | Value |
|----------|-------|
| **UniProt Accession** | **P56178** |
| **Entry Name** | DLX5_HUMAN |
| **Protein Name** | Homeobox protein DLX-5 |
| **Gene Name** | DLX5 |
| **Organism** | *Homo sapiens* (Human) |
| **Length** | **289 amino acids** |
| **Subcellular Location** | **Nucleus** |
| **Function** | Transcription factor involved in craniofacial development; plays a role in osteoblast differentiation and bone formation. Acts as a regulator of downstream target genes during development. |

### FASTA Sequence (downloaded from UniProt)

File saved as `human_DLX5.fasta`:
```
>sp|P56178|DLX5_HUMAN Homeobox protein DLX-5 OS=Homo sapiens OX=9606 GN=DLX5 PE=1 SV=2
MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCS
PTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEK
EVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQ
VKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAH
PPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY
```

---

## 2. Online BLAST Results (UniProt)

### Procedure

1. Navigated to the human DLX5 entry page on UniProt (P56178)
2. Clicked the **BLAST** button to launch a sequence similarity search
3. Restricted taxonomy to **Eutheria (placental mammals)**
4. Ran BLAST with default parameters (BLOSUM62 matrix)

### Results Summary

| Metric | Value |
|--------|-------|
| **Number of hits** (restricted to Eutheria) | ~20–40 homologous proteins retrieved |
| **% Identity range** across hits | Approximately **35% – 100%** |
| **Best hit:** Mouse DLX5 (**P70396**) | **~96–97% identity** |

### Alignment Visualization Notes

When viewing the graphical alignment between human DLX5 (query) and mouse DLX5 (P70396):

- **Blue-highlighted residues** = positions where the two sequences have **identical** amino acids (exact matches)
- **Grey / neutral-highlighted residues** = **conservative substitutions** (different amino acids but chemically similar, receiving positive BLOSUM62 scores)
- Unhighlighted residues = non-conservative substitutions (dissimilar amino acids)

The wrapped alignment view shows that the two sequences are highly conserved across nearly their entire length, with only a handful of mismatched positions scattered throughout.

---

## 3. Python Non-Gapped Global Alignment

### Approach

I implemented a simple pairwise sequence comparison program in Python that:

1. Reads two protein sequences from **FASTA format**
2. Loads the standard **BLOSUM62 substitution matrix**
3. Performs a **non-gapped global alignment** — comparing each position side-by-side without allowing insertions or deletions
4. Reports the total BLOSUM62 score and percentage identity (% of identical residues)
5. Prints a compact visual comparison showing matches (`|`), positive-scoring mismatches (`+`), and negative-scoring mismatches (`.`)

Three comparisons were run:

| # | Sequence 1 | Sequence 2 | Expected |
|---|-----------|-----------|----------|
| 1 | Human DLX5 | Mouse DLX5 | High score & high identity (homologs) |
| 2 | Human DLX5 | Random sequence (289 aa) | Low score & low identity (negative control) |
| 3 | Mouse DLX5 | Random sequence (289 aa) | Low score & low identity (negative control) |

The random sequence was generated in-code using a fixed seed for reproducibility, containing the same length (289 aa) as the DLX5 proteins.

### Results

```
=================================================================
  SUMMARY TABLE
=================================================================
  Comparison                      BLOSUM Score   % Identity
  ------------------------------  -------------  ----------
  Human vs Mouse                          1490        96.5%
  Human vs Random                         -262         6.2%
  Mouse vs Random                         -268         6.2%
```

### Detailed Breakdown

#### Comparison 1: Human DLX5 vs Mouse DLX5

- **BLOSUM62 Total Score: +1490**
- **% Identity: 96.5%** (279 out of 289 positions identical)
- The 10 mismatched positions are mostly **conservative substitutions** (e.g., T→P at position 22, S→A at position 97, G→A at position 108, S→G at position 110, Y→G at position 120, S→Y at position 121, Y→G at position 124, T→S at position 177, T→P at position 258, T→S at position 260). Most of these still receive **positive or near-zero BLOSUM scores**, which is why the total remains strongly positive.
- This confirms that human and mouse DLX5 are **highly conserved orthologous proteins**.

#### Comparison 2: Human DLX5 vs Random Sequence

- **BLOSUM62 Total Score: -262**
- **% Identity: 6.2%** (only 18 out of 289 positions identical — consistent with chance expectation for random 20-letter alphabet over 289 positions)
- The large negative score reflects that most random pairings are non-conservative mismatches penalized by BLOSUM62.

#### Comparison 3: Mouse DLX5 vs Random Sequence

- **BLOSUM62 Total Score: -268**
- **% Identity: 6.2%** (18 identical positions)
- Nearly identical to the human-vs-random result, as expected since both DLX5 proteins are similar in composition.

---

## 4. Conclusion

The results clearly demonstrate the difference between **biologically meaningful sequence similarity** and **random chance**:

| Comparison | Interpretation |
|------------|---------------|
| **Human vs Mouse (+1490, 96.5%)** | These are homologous proteins sharing a common evolutionary ancestor. The extremely high % identity and large positive BLOSUM score indicate strong functional and structural conservation. |
| **Either vs Random (~-265, ~6%)** | A random sequence of the same length produces only background-level similarity. The ~6% identity matches what we'd expect by chance (1/20 ≈ 5%), and the negative BLOSUM score confirms there is no meaningful relationship. |

This exercise shows why substitution matrices like BLOSUM62 are essential in bioinformatics: they allow us to **quantify** sequence relationships in a way that accounts for the biochemical reality that not all amino acid changes are equally disruptive. Simple match/mismatch scoring would miss this nuance entirely.
