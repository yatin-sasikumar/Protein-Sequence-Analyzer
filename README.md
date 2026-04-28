# Protein-Sequence-Analyzer

## Overview
A Python-based tool to analyze protein sequences from FASTA files. It computes key biochemical properties and generates an Excel report with embedded hydrophobicity plots.

## Features
- Reads protein sequences from FASTA  
- Calculates:
  - Length  
  - Amino acid composition (%)  
  - Molecular weight  
  - Isoelectric point (pI)  
  - GRAVY score  
  - Instability index  
  - Aromaticity  
  - Secondary structure (helix, turn, sheet)  
- Generates hydrophobicity plots (Kyte–Doolittle)  
- Outputs a structured Excel file with plots  

## Usage
1. Place your FASTA file (e.g., `input.fasta`)  
2. Run:
   ```bash
   python main.py


## Input
The input should be a FASTA file containing one or more protein sequences.
Example: 
   ```text
   >Protein_1
   MKTFFVLLLCTFTVVSA
```
## Output
The program generates an Excel file (`output.xlsx`) containing:
- Protein name  
- Amino acid composition (%)  
- Physicochemical properties:
  - Length  
  - Molecular weight  
  - Isoelectric point (pI)  
  - GRAVY score  
  - Instability index  
  - Aromaticity  
  - Secondary structure (helix, turn, sheet)  
- Hydrophobicity plot for each protein embedded alongside the data

## Tech Stack
- Python  
- Biopython  
- OpenPyXL  
- Matplotlib  

