with open('test.txt','r') as f :
    f = f.read()
f = f.replace('\n',' ').strip('.,?:-!').split(' ')
words =[' ']
for word in f:
    if word in words :
        pass
    else:
        print(word, f.count(word))
        words.append(word)
