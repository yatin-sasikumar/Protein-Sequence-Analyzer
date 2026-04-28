from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import csv

# Input and Output files
input_fasta = "input.fasta"
output_csv = "output.csv"

# Open CSV file
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow([
        "Protein_ID",
        "Length",
        "Molecular_Weight",
        "Isoelectric_Point",
        "GRAVY",
        "Instability_Index",
        "Aromaticity",
        "Helix",
        "Turn",
        "Sheet"
    ])

    # Read FASTA
    for record in SeqIO.parse(input_fasta, "fasta"):
        seq = str(record.seq)
        analysis = ProteinAnalysis(seq)

        length = len(seq)
        mw = analysis.molecular_weight()
        pI = analysis.isoelectric_point()
        gravy = analysis.gravy()
        instability = analysis.instability_index()
        aromaticity = analysis.aromaticity()

        # Secondary structure fraction
        helix, turn, sheet = analysis.secondary_structure_fraction()

        # Write row
        writer.writerow([
            record.id,
            length,
            round(mw, 2),
            round(pI, 2),
            round(gravy, 3),
            round(instability, 2),
            round(aromaticity, 3),
            round(helix, 3),
            round(turn, 3),
            round(sheet, 3)
        ])

print("Analysis complete. Results saved to output.csv")