from Bio import SeqIO
seq=[]
final=[]
finalfinal = []

with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        seq.append(str(record.seq))
truc= str(seq[0])
truc2= str(seq[1])
autre = str(seq[2:len(seq)])
def compare():
    for i in range(len(truc)):
        for j in range(len(truc2)-i+1,1,-1):

            # print(truc,'\n',truc2,'\n',truc[i:i+j], '\n',truc2.find(truc[i:i+j])>0,'\n')
            if truc2.find(truc[i:i+j+1])>0 and truc[i:i+j] not in final:
                final.append(truc[i:i+j+1])


def comparewithother(i):
    for substring in final :
        machin = str(seq[i])
        # print(machin)
        # print(substring,'\n', machin,'\n',machin.find(substring) >0)
        if machin.find(substring) >0 :
            finalfinal.append(substring)

compare()

for i in range(2,len(seq)):
    comparewithother(i)

print(max(finalfinal,key=len))
