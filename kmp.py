from Bio import SeqIO
seq=[]

with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        seq.append(str(record.seq))
seq = seq[0]
faillurearray = []
fail = []

count = 0
##choisi le prefix (ex: ATG = A 0, AAT= AA 0 1)
while seq[count] == seq[0]:
    fail.append(seq[count])
    faillurearray.append(count)
    count+=1
for i in range(len(fail),len(seq)):
    print(seq[i])
    if seq[i] == fail[i%len(fail)]:
        print(seq[i], len(fail),seq[i] == fail[i%len(fail)])
print(fail)
print(faillurearray)
