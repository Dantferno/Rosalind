from Bio import SeqIO
import numpy as np
lt={}
seq=[]

with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        lt[str(record.id)] = str(record.seq)
        seq.append(str(record.seq))
    #lt {id:seq}
    #seq =[seq1, seq2]
seq = list(seq[0])
reverse_seq = list(record.seq.reverse_complement())
startpos = []
stoppos = []
ORF = []
##identifie les positions des codons stop et start, choisie le plus petit codon %3 etstock dans ORF
for i in range(len(seq)-2):
    if seq[i] =='A' and seq[i+1]=='T' and seq[i+2]=='G':
        startpos.append(i)
    elif  seq[i] =='T' and seq[i+1]=='A' and seq[i+2]=='G':
        stoppos.append(i)
    elif  seq[i] =='T' and seq[i+1]=='G' and seq[i+2]=='A':
        stoppos.append(i)
    elif  seq[i] =='T' and seq[i+1]=='A' and seq[i+2]=='A':
        stoppos.append(i)
for i in startpos :
    for j in stoppos :
        if (j- i)%3==0 and (j- i)>0:
            ORF.append(seq[i:j])
            break
##Pareil mais pour la reverse strand
startpos = []
stoppos = []
for i in range(len(reverse_seq)-2):
    if str(reverse_seq[i])+str(reverse_seq[i+1])+str(reverse_seq[i+2]) == 'ATG':
        startpos.append(i)
    elif  str(reverse_seq[i])+str(reverse_seq[i+1])+str(reverse_seq[i+2]) == 'TAG':
        stoppos.append(i)
    elif  str(reverse_seq[i])+str(reverse_seq[i+1])+str(reverse_seq[i+2]) == 'TGA':
        stoppos.append(i)
    elif  str(reverse_seq[i])+str(reverse_seq[i+1])+str(reverse_seq[i+2]) == 'TAA':
        stoppos.append(i)
for i in startpos :
    for j in stoppos :
        if (j- i)%3==0 and (j- i)>0:
            ORF.append(reverse_seq[i:j])
            break
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
#transforme les ORF ADN en ORF Acide aminé
trad = []
final=[]
for i in range(len(ORF)):
    B="".join(ORF[i])
    for j in range(len(B)):
        if j%3 ==0:
            # print(B, i ,j,B[j:j+3] )
            x = gencode.get(B[j:j+3])
            trad.append(x)
    final.append(trad)
    trad = []
##Enleve les duplicates de la liste final et met les uniques dans protfinal
protfinal =[]
for prot in final:
    if prot not in protfinal:
        protfinal.append(prot)

print('ORF :')
for i in range(len(protfinal)):
    print(''.join(protfinal[i]))
