import sys
final=[]
stop = 3
dic = { 'G': 4, 'A': 4, 'V': 4, 'L': 6, 'I': 3, 'P': 4, 'F': 2, 'Y': 2, 'W': 1, 'S': 6, 'T': 4, 'C': 2, 'M': 1, 'N': 2, 'Q': 2, 'K': 2, 'R': 6, 'H': 2, 'D': 2, 'E': 2, 'B': 4, 'Z': 4 }

with open('test.fasta','r') as f:
    prot = f.readline().strip('\n')

for aa in prot:
    final.append(dic.get(aa))

total=1
for i in final:
    total *= i
    # if total%1000000 >=1:
    #     total = total%100

print((total*3)%1000000)
