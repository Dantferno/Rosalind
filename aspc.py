import math
with open('test.txt','r') as f:
    f =f.readlines()
    f =f[0].strip('\n').split(' ')
n= int(f[0])
m=f[1]
def combination(n,k):
    return math.factorial(n)//(math.factorial(k)*math.factorial((n-k)))

sum = 0
for i in range(int(m),n+1):
    sum += combination(n,i)
print(int(sum)%1000000)
