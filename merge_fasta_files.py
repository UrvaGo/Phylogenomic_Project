import os
from Bio import SeqIO
#to merge fasta file into a single fasta file
folder_path = r"Replace with the path to your folder containing the FASTA files"
output_file = "Replace with the desired output file path" 

# Get a list of all FASTA files in the folder
fasta_files = [f for f in os.listdir(folder_path) if f.endswith(".fasta")]

# Open the output file in write mode
with open(output_file, "w") as merged_fasta:
    # Iterate over each FASTA file
    for fasta_file in fasta_files:
        fasta_path = os.path.join(folder_path, fasta_file)
        # Open each input FASTA file and append its records to the merged file
        with open(fasta_path, "r") as input_fasta:
            for record in SeqIO.parse(input_fasta, "fasta"):
                SeqIO.write(record, merged_fasta, "fasta")

print("FASTA files merged successfully!")
