from Bio import SeqIO
import numpy as np
seqs=[]


with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        seqs.append(str(record.seq))

#récupere toutes les substrings de taille 1/2len(seq) pour une sequence donnée
def substring(seq):
    list =[]
    taille = int((1/2)*len(seq))
    for i in range(len(seq)):
        if len(seq[i:i+taille]) == taille:
            list.append(seq[i:i+taille])
    return list

substrings = np.empty([len(substring(seqs[0]))])

def search(seq1):
    #pour chaque set de substring de la sequence1, test si une substring est présent dans toutes les autres seq
    for seqspecifiq in substrings:
        
#stock dans une matrice les substrings (une seq par ligne, n substring colonness)
for seq in seqs:
    a = substring(seq)
    a = np.asarray(a)
    substrings = np.vstack((substrings, a))
substrings = substrings[1:]

for i in substrings :
    print(i)
