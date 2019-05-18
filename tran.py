from Bio import SeqIO
import numpy as np
lt={}
seq=[]

with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        seq.append(str(record.seq))
print(seq)

def compare(string1,string2):
    transition =0
    transversion =0
    st1,st2 = list(string1),list(string2)
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            if st1[i]=='A' and st2[i]=='G' or st1[i]=='G' and st2[i]=='A':
                transition +=1
            elif st1[i]=='C' and st2[i]=='T' or st1[i]=='T' and st2[i]=='C':
                transition +=1
            else:
                transversion +=1
    print(transition,transversion)
    return transition/transversion
print(compare(seq[0],seq[1]))
