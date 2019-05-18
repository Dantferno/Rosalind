from Bio import SeqIO
seq=[]
final=[]
finalfinal =[]
with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        seq.append(str(record.seq))

def verif(n2,final):
    for i in range(len(seq[0])):
        for j in range(len(seq[0])-i+1,1,-1):
            truc= str(seq[0])
            truc2= str(seq[n2])
            # print(truc[i:i+j],truc2,truc2.find(truc[i:i+j])>0, i, i+j)
            # print(truc,'\n',truc2,'\n',truc[i:i+j], '\n',truc2.find(truc[i:i+j])>0,'\n')
            if truc2.find(truc[i:i+j])>0 and truc[i:i+j] not in final:
                final.append(truc[i:i+j])
                # print(final)
    finalfinal.append(final)
    final = []


def countX(lst, x):
    return lst.count(x)


for i in range(1,len(seq)):
    verif(i,final)
    final = []
fin = []
# for i in finalfinal:
#     print(str(finalfinal),i, countX(final,i),len(seq)-1)
    # if countX(finalfinal,i) == len(seq)-1:
    #     print(i,countX(finalfinal,i) == len(seq)-1 )
    #     fin.append(i)
for i in finalfinal:
    for j in i:
        fin.append(j)
c=0
longest = {}
for i in fin:
    if countX(fin,i) >c:
        c= countX(fin,i)
        longest[countX(fin,i)] = i
print(longest)
print(c)
print(longest.get(c))
