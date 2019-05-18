from Bio import SeqIO
import itertools

nombre = int(input('Integer : \n'))
set =[1]
def factoriel(n):
    #calcul factoriel de n et crée son set
    fac =1
    for i in range(2,n+1):
        fac *= i
        set.append(i)
    return fac

print(factoriel(nombre))
permutation = list(itertools.permutations(set))
with open('test.fasta','w') as f:

    for permut in permutation:
        permut = str(permut).strip('()')
        print(permut.replace(',',''), file=f)

# def permutation():
