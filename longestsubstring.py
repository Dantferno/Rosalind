from Bio import SeqIO
lt={}
seq =[]
longyet = []
longest = []

with open("test.fasta", "r") as f:
    #met les fastas dans un dico {id: seq}
    for record in SeqIO.parse(f, "fasta"):
        lt[str(record.id)] = str(record.seq)
        seq.append(str(record.seq))
    #lt {id:seq}
    #seq =[seq1, seq2]
    decomp = list(seq[0])
    decomp2 = list(seq[1])
    for i in decomp:
        t=0
        for j in decomp2:
            v=0
            print(i,j)
            if i == j :
                t+=1
                v+=1
                longyet.append(j)
                for n in range(len(decomp)):
                    if decomp[t+n] == decomp2[v+n]:
                        longyet.append(decomp[t+n])

            print(longyet)
