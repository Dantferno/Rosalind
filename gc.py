#!/bin/python
from Bio import SeqIO
records = list(SeqIO.parse("test.fasta", "fasta"))
for i in range(len(records)):
	print(records[i].id)
	count = 0
	for nuc in records[i].seq:
		if nuc == 'C':
			count += 1
		else:
			pass
		if nuc == 'G':
			count += 1
		else:
			pass
	print((count/len(records[i].seq)*100))
	

