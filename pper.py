from math import*

n=99
k=8
def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)
print(fact(n)/fact(n-k)%1000000)
