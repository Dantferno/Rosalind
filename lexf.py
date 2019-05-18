import itertools
with open('test.fasta','r') as f:
    f = f.readlines()
alphabet = f[0].strip('\n').split(' ')
longueur = int(f[1].strip('\n'))
fin = list(itertools.permutations(alphabet, longueur))
final = []
for i in fin:
    final.append(''.join(i))
for i in alphabet:
    final.append('{0}{1}'.format(i,i))
final.sort()
for i in final:
    print(i)
