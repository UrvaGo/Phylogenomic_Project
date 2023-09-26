from Bio import pairwise2
from Bio.Seq import Seq
import os
from Bio.pairwise2 import format_alignment 

# Creating sample sequences
input_dir1 = r"D:\user\Desktop\first_file.fasta"
input_dir2 = r"D:\user\Desktop\second_file.fasta"
output_dir = r"D:\user\Desktop\out_file"
match=[]
for file1 in os.listdir(input_dir1):
    os.chdir(input_dir1)
    input_path1 = os.path.join(input_dir1, file1)
    org = file1.split("")
    genes = SeqIO.parse(input_path1, 'fasta')
    gene_dict = {}
    for gene in genes:
        gene_dict[gene.id] = str(gene.seq)

os.chdir(input_dir2)
input_path2 = os.path.join(input_dir2, file2)
gene_file2 = SeqIO.parse(input_path2, 'fasta')
recs = file2.split()
for name, seq in gene_dict.items():
    name = gene_dict[name.id]

    alignments = pairwise2.align.globalxx(input_dir1, input_dir2)
    for match in alignments:
        match.append(alignmets)
        print(match)
    os.chdir(output_dir)
    output_path = os.path.join(output_dir, out_file)
    with open(out_file, 'w') as fout:
        fout.write()

