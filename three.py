with open('test.txt','r') as edges:
    edges =edges.readlines()
    noeud = edges.pop(0).strip('\n')
print((int(noeud)-1)-len(edges))
