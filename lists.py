stuff=list()
stuff.append('book')
stuff.append(99)
print(stuff)


# Finding average
numlist= list()
while True:
    inp=input('Enter a number:')
    if inp=='done': break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print('Average:', average)


# Split
abc='With three words'
stuff=abc.split()
print(stuff)
for w in stuff:
    print(w)

# Split for mail parsing
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'): 
        continue 
    words=line.split()
    print(words[2])


friends=['Glenn', 'Max', 'Sally']
print(friends[2])

