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
    sum =0
    st1,st2 = list(string1),list(string2)
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            sum +=1
    sum = (sum/len(seq[0]))
    return round(sum,5)
matrice = []
for i in range(len(seq)):
    for j in range(len(seq)):
        matrice.append(compare(seq[i],seq[j]))
matrice = np.matrix(matrice)
matrice = np.reshape(matrice,(len(seq),len(seq)))
for i in matrice:
    print(str(i).strip('[]'))
