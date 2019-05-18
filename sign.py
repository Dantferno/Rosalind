import itertools
a = input('n = ')
a = range(1,int(a)+1)
print(list(itertools.permutations(a)))
