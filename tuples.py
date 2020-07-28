d=dict()
d['csev']=2
d['cwen']=4
for (k,v) in d.items():
    print(k,v)
tups = d.items()
print(tups)


# sorted by key
d={'a': 10, 'b': 1, 'c': 22}
t= sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v)


# sorted by value 
c={'a': 10, 'b': 1, 'c': 22}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp)


# Top ten most common  word
fhand=open('romeo.txt')
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word, 0)+1 
lst=list()
for key, val in counts.items():
    newtup=(val,key)
    lst.append(newtup)

lst=sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)


x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])