#!/bash/python
a = input('rentre k, m et n : ex: 2 2 2 : \n')
kmn = a.strip().split()
k, m, n = kmn[0], kmn[1], kmn[2]
poptot = int(k)+int(m)+int(n)
k, m, n = int(k),int(m),int(n)
dominant = ((k*k - k) + 2*(k*m) + 2*(k*n) + (.75*(m*m - m)) + 2*(.5*m*n))/((k + m + n)*(k + m + n -1))
print(dominant)



