#To parse the blast result as fasta file
from Bio import SeqIO
import os

fasta_file = r"path_to _fasta file"
output_path = r"path_ to_output"
blast_result = r"path_to_blast_table"

seqid_to_name = {}
#open the blast text file (output fmt6)
with open(blast_result, 'r') as fin:
    for line in fin:
        line_l = line.split()
        seqid_to_name[line_l[1]]=line_l[0]
#open the fasta file to parse the result
recs = SeqIO.parse(fasta_file, 'fasta')
recs_to_write=[]
for rec in recs:
    if rec.id in seqid_to_name:
        rec.id = seqid_to_name[rec.id]
    #print(rec.id)
        recs_to_write.append(rec)
        print(recs_to_write)
# write the fasta file
SeqIO.write(recs_to_write,"protein",'fasta')