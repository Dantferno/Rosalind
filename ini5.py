with open('test.txt','r') as f:
    f = f.readlines()
for linenumber in range(1,len(f)):
    if linenumber % 2 != 0:
        print(f[linenumber].strip('\n'))
