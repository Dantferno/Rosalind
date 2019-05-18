from Bio import SeqIO
import math
seq =[]
reverse =[]
with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        seq.append(str(record.seq))
        reverse.append(str(record.seq.complement()))

seq, reverse = str(seq).strip('[\']'), str(reverse).strip('[\']')
print(seq,'\n',reverse)
a =[]
for i in range(len(seq)+1):
    for j in range(4,13):
        reversestring =reverse[i:i+j]
        reversestring = reversestring[::-1]
        # print(reversestring, seq[i:i+j], i+1,j, i+j+1)
        if reversestring == seq[i:i+j] and len(reversestring)>=4 and i+j<=len(seq) :
            print(i+1,len(reversestring))
