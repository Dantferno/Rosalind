import itertools
from Bio import SeqIO
seqs = []
with open('test.fasta','r') as f:
    for record in SeqIO.parse(f, "fasta"):
        seqs.append(str(record.seq))

alphabet = 'ATGC'
Klongueur = 4
kmers = list(itertools.product(alphabet, repeat = 4))
final = []
for i in kmers:
    final.append(''.join(i))
final.sort()
mondic = {}
for i in final:
    print(seqs[0], seqs[0].count(i), i , seqs[0].count('AAAA'),'AAAA')
    mondic[i] = seqs[0].count(i)
finfin = []
for i in mondic:
    finfin.append(mondic[i])
print(str(finfin).strip('[]').replace(',',''))
