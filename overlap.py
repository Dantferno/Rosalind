#!/bin/python
from Bio import SeqIO
lt = {}
ll = {}
a=[]
n=[]
with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        lt[str(record.id)] = str(record.seq)
    #pour chaque sequence, x prend la sequence et les pref et suff sont enregistré dans une liste ll
    for i in lt:
        x = str(lt[i])
        pref, suff = x[:3], x[len(x)-3:len(x)]
        ll[i] = pref, suff
    #met les prefixes et suffixes dans deux listes apart
    for i in ll:
        pref, suff = ll[i]
        a.append(pref.split('\n'))
        n.append(suff.split('\n'))
    deg = list(ll) #store les id dans une liste
    #check si un prefixe match avec suffixe autre que lui meme et sort l'id des matchs ID1 ID2
    file = open('test.txt','w')
    for i in range(len(a)):
        for j in range(len(n)):
            if i != j:
                if a[i] == n[j]:
                    # print le nom des ieme prefixe et le jieme suffixe qui match
                    print(deg[j],',',deg[i],'\n')
                    file.write(deg[j])
                    file.write(',')
                    file.write(deg[i])
                    file.write('\n')
                    print(deg[j],',',deg[i],'\n')









        # ll.append(i).append()
        # if lt[i]
        # print(lt[i])
