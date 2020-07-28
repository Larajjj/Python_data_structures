purse=dict()
purse['money']= 12
purse['candy']= 3
purse['tissues']= 75
print(purse)


# Counting 
counts=dict()
names=['csev', 'cwen', 'csev', 'zqian','cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)


# Simplified Counting with .get()
counts=dict()
names=['csev', 'cwen', 'csev', 'zqian','cwen']
for name in names:
    counts[name]=counts.get(name, 0)+1
print(counts)


stuff=dict()
print(stuff.get('candy', -1))


# The first program
name=input('Enter file:')
handle=open(name)

counts=dict()
for line in handle:
    words=line.split()
    for word in  words:
        counts[word]= counts.get(word,0)+1

bigcount=None
bigword=None
for word, count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword, bigcount) 
