import os
# to collect the first hit from the blast outfmt 6
input_dir = r"D:\user\Desktop\New_data\craspedacusta\Craspedacusta_reciprocal"
out_dir = r"D:\user\Desktop\New_data\craspedacusta"
hits = []

# open the input file to read

for file in os.listdir(input_dir):
    os.chdir(input_dir)
    with open(file, 'r')as f:
        best_hit = f.readline()
        hits.append(best_hit)
# open the output file

os.chdir(out_dir)
with open('reciprocal_blast.txt', 'w')as s:
    for line in hits:
        s.write(line)


