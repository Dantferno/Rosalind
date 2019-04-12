from Bio import SeqIO
import numpy as np
lt={}
seq=[]
vecteurstring = []
a =np.array([[]])
tmp = []
A,T,G,C = 0,0,0,0
profile =[]
consensus = ''
with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        lt[str(record.id)] = str(record.seq)
        seq.append(str(record.seq))
    #lt {id:seq}
    #seq =[seq1, seq2]
a = []
#stoque chaque seqence comme une ligne dans la matrice a
for i in seq :
    c =list(i)
    a.append(c)
a = np.array(a)
#compte les ATGC de chaque colonne et crée la matrice profile
for i in range(len(a[0])):
    for j in range(len(seq)):
        #tmp stock les nieme nucleotides de chaque string
        tmp.append(a[j,i])

    A,T,G,C = tmp.count('A'), tmp.count('T'),tmp.count('G'),tmp.count('C')
    #tmp stock le nombre de ATGC a la position i de chaque string et l'ajoute a profile
    tmp=[A,C,G,T]

    #rajoute a consensus le nucleotide le plus abondant a la position i
    consensus += {0: 'A', 1: 'C', 2: 'G', 3: 'T'}.get(tmp.index(max(tmp)))
    profile.append(tmp)
    tmp=[]

profile =np.array(profile)
profile = np.transpose(profile)
print(consensus)
print('A:', str(profile[0]).strip('[]'), '\n','C:', str(profile[1]).strip('[]'), '\n',
'G:', str(profile[2]).strip('[]'), '\n',
'T:', str(profile[3]).strip('[]'),end='')
