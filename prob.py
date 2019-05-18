import math
with open('prob.txt','r') as f:
    f = f.read()
    f = f.split('\n')
    seq = f[0]
    GCcontent = f[1].split()


def GCATtoproba(GC):
    return float(GC)/2, (1-float(GC))/2

def testdna(probaGC, probaAT):
    proba = 1
    for i in seq :
        if i == 'C':
            proba *= probaGC
        elif i == 'G':
            proba *= probaGC
        else:
            proba *= probaAT
    return math.log(proba,10)

final = []
for i in GCcontent:
    probaGC, probaAT = GCATtoproba(i)
    proba = testdna(probaGC, probaAT)
    final.append(round(proba,3))
final = str(final)
final = final.replace(',', '').strip('[]')
print(final)
