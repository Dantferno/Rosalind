with open('test.txt','r') as sets:
    sets =sets.readlines()
    n = sets.pop(0).strip('\n')
    set1 = sets[0].strip('\n {}').replace(',','').split(' ')
    set2 = sets[1].strip('\n {}').replace(',','').split(' ')
    set1, set2= set(set1),set(set2)
setcompletment = [str(i) for i in range(1,int(n)+1)]
setcompletment = set(setcompletment)

print(str(set1.union(set2)).replace("'", ""))
print(str(set1.intersection(set2)).replace("'", ""))
print(str(set1.difference(set2)).replace("'", ""))
print(str(set2.difference(set1)).replace("'", ""))
print(str(setcompletment.difference(set1)).replace("'", ""))
print(str(setcompletment.difference(set2)).replace("'", ""))
# print(set1,set2,type(set1))
