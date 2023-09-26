#extract info from fasta file
import os
import pandas as pd
from Bio import SeqIO
#to make a table from fasta file with gene and gene description details

folder_path = r"D:\user\Desktop\folder_name"
file_path = r"D:\user\Desktop\merge_folder\fasta_file"
genes = extract_gene_info_from_fasta(file_path)

def extract_gene_info_from_fasta(file_path):
    gene_info = []

    for record in SeqIO.parse(file_path, "fasta"):
        gene_name = record.id.rstrip()
        gene_description = record.description
        gene_info.append((gene_name, gene_description, file_name))
    return gene_info

# Create a DataFrame from the gene information
df = pd.DataFrame(genes, columns=["Gene Name", "Gene Description", "file_name"])

# Save the DataFrame to an Excel file
output_file = "gene_info.xlsx"
df.to_excel(output_file, index=False)
print(f"Gene information saved to {output_file}")


extract_gene_info_from_fasta(file_path)
