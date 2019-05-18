from Bio import SeqIO
import math
lt={}
seq=[]

with open("test.fasta", "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        seq.append(str(record.seq))
print(math.factorial(seq[0].count('A'))*math.factorial(seq[0].count('G')))
