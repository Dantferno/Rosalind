#!/bin/python
with open('test.fasta','r') as f:
	f = f.read().strip().split()
	string = f[0]
	substring = f[1]
	final = []
	count =0
	j = 0
	liist = []
	
	for i in range(len(string)):
		final.append(string[i:i+len(substring)])
	
	for i in final:
		j += 1
		if i == substring:
			liist.append(j)
	liste = str(liist)
	print(''.join(liste))
	
