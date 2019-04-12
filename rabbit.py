mois=29
a=5
liste= [1,1]
tot = 0
for i in range(mois-2):
    c = a*liste[i]+liste[i+1]
    liste.append(c)
    tot += c
    print(liste)
