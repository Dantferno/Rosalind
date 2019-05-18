import urllib.request
from Bio import SeqIO

fasta = []

def chopefasta(prot):
    with urllib.request.urlopen('http://www.uniprot.org/uniprot/{}.fasta'.format(prot)) as response:
        html = response.read().decode('UTF-8')
        fasta.append(html.split(' '))

with open('test.fasta','r') as f:
    f =f.read().split()
    for prot in f:
        chopefasta(prot)
print(fasta)
#N{P}[ST]{P}
