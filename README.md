# Protein-Sequence-Analyzer

# Overview
A Python-based tool to analyze protein sequences from FASTA files. It computes key biochemical properties and generates an Excel report with embedded hydrophobicity plots.

# Features
Reads protein sequences from FASTA
Calculates:
   Length
   Amino acid composition (%)
   Molecular weight
   Isoelectric point (pI)
   GRAVY score
   Instability index
   Aromaticity
   Secondary structure (helix, turn, sheet)
   Generates hydrophobicity plots (Kyte–Doolittle)
   Outputs a structured Excel file with plots

# Usage
Place your FASTA file (e.g., input.fasta)
Run:
   python main.py
Output: output.xlsx
Input Format
    >Protein_1
    MKTFFVLLLCTFTVVSA
Output
  Excel file with:
    Composition
    Protein properties
    Hydrophobicity plot for each protein
    
# Tech Stack
Python
Biopython
OpenPyXL
Matplotlib
