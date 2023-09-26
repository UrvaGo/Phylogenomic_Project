import os
import pandas as pd

# to compare the two blast output (outfmt 6)

file1 = r"D:\user\Desktop\Table\Hydra.txt"
file2 = r"D:\user\Desktop\Table\Henneguya_miniprot_reciprocal.txt" 

list1 = []
#open the first file
with open(file1, "r")as f_in: 
    check_lines = f_in.readlines()

    for i in range(len(check_lines)):
        geneID2 = check_lines[i]
        gene_name = geneID2.split("\t")[0].strip()
        accession = geneID2.split("\t")[1].strip()
        data = (gene_name, accession)
        list1.append(data)
        #print(data)


#Dupes = []
list2 = []
# open the second file to compare
with open(file2, "r")as f:
    s_lines = f.readlines()

    for i in range(len(s_lines)):
        geneID = s_lines[i]
        gene_name2 = geneID.split("\t")[0].strip()

        accession2 = geneID.split("\t")[1].strip()
        data2 = (gene_name2, accession2)
        list2.append(data2)

print("Additional values in second list:", (set(list2).difference(list1)))
print("Missing values in second list:", (set(list1).difference(list2)))