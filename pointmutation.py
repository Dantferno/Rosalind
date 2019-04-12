#!/bin/python
seq = []
count = 0
with open("test.fasta","r") as f:
	raw = f.readlines()
	for i in raw:
		b= i.strip('\n').split()
		seq.append(b)
	seq1, seq2 = list(seq[0]), list(seq[1])
	for x, y in zip(list(seq1[0]), list(seq2[0])):
		if x != y:
			count +=1
	print(count)
