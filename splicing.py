from Bio import SeqIO, Seq
import numpy as np

seq=[]

with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        seq.append(str(record.seq))
    #lt {id:seq}
    #seq =[seq1, seq2]
motherstring = seq[0]
substring = seq[1:len(seq)]


for introns in substring:
    motherstring = motherstring.replace(introns,'')

print(Seq.translate(motherstring))
